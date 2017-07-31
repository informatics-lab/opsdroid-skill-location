from opsdroid.matchers import match_apiai_action
import logging
import random

import aiohttp

_LOGGER = logging.getLogger(__name__)

def get_location_svc_url(config):
    return config.get("url", "http://localhost:5000")

@match_apiai_action("labby.lab.setlocation")
async def where_are_you(opsdroid, config, message):
    """Ask users where they are."""
    location_svc_url = get_location_svc_url(config)
    if not message.apiai["result"]["parameters"]["location"]:
        await message.respond("Pardon?")
    else:
        location = message.apiai["result"]["parameters"]["location"].capitalize()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    '{}/user/{}'.format(location_svc_url, message.user),
                    json={'location': location},
                    headers={"Authorization": "Bearer {}".format(config["auth-token"])}) as resp:
                    if resp.status >= 400:
                        raise ValueError("Bad return code %i", resp.status)
                    else:
                        _LOGGER.info("Set location of %s to %s", message.user, location)
                        await message.respond("Ah thanks! I've updated your location to '{}'".format(location))
        except (ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
            _LOGGER.error(e)
            await message.respond("Hmm I couldn't update you location, try again later.")
        except KeyError as e:
            _LOGGER.error(e)
            await message.respond("Sorry can't do that! You need to set an 'auth-token' in the config.")


@match_apiai_action("labby.lab.getlocation")
async def where_is_labby(opsdroid, config, message):
    """Say where a user is."""
    location_svc_url = get_location_svc_url(config)
    if not message.apiai["result"]["parameters"]["person"]:
        await message.respond("Who?")
    else:
        person = message.apiai["result"]["parameters"]["person"]
        async with aiohttp.ClientSession() as session:
            async with session.get('{}/user/{}'.format(location_svc_url, person)) as resp:
                location = await resp.json()
                await message.respond("{} is in the {}".format(person, location["location"]))
