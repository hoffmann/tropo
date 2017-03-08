from tropo.compute import *
from tropo.base import dump


def test_osdisk():
    od = OsDisk(
        name="osdisk",
        image={"uri": "uri"},
        caching="None",
        createOption="FromImage",
        vhd=Vhd("uri"),
        osType="Linux")

    expected = {
        "name": "osdisk",
        "vhd": {
            "uri": "uri"
        },
        "osType": "Linux",
        "image": {
            "uri": "uri"
        },
        "caching": "None",
        "createOption": "FromImage"
    }
    assert dump(od) == expected


def test_datadisk():
    dd = DataDisk(
        name="datadisk0",
        diskSizeGB=1000,
        createOption="Empty",
        caching="None",
        lun=0,
        vhd=Vhd("uri"))

    expected = {
        "name": "datadisk0",
        "diskSizeGB": 1000,
        "lun": 0,
        "vhd": {
            "uri": "uri"
        },
        "caching": "None",
        "createOption": "Empty"
    }
    assert dump(dd) == expected


def test_network_profile():
    network_profile = NetworkProfile([{"id": "resourceid"}])

    expected = {
        "networkInterfaces": [
            {
                "id": "resourceid"
            }
        ]
    }
    assert dump(network_profile) == expected


def test_vhd():
    vhd = Vhd(uri="https://storage.blob.core.windows.net/vhds/osdisk.vhd")

    expected = {
        "uri": "https://storage.blob.core.windows.net/vhds/osdisk.vhd"
    }
    assert dump(vhd) == expected
