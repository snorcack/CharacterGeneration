{
  "id": "19706893-a18e-4f36-9dde-a812d5bbe601",
  "revision": 0,
  "last_node_id": 834,
  "last_link_id": 1315,
  "nodes": [
    {
      "id": 343,
      "type": "SetNode",
      "pos": [
        545.9968815123061,
        5014.679804289289
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 105,
      "mode": 0,
      "inputs": [
        {
          "name": "MODEL",
          "type": "MODEL",
          "link": 639
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_LTXModel",
      "properties": {
        "previousName": "LTXModel",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "LTXModel"
      ],
      "color": "#223",
      "bgcolor": "#335",
      "shape": 1
    },
    {
      "id": 342,
      "type": "SetNode",
      "pos": [
        549.0798478398342,
        4964.0718778009905
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 104,
      "mode": 0,
      "inputs": [
        {
          "name": "VAE",
          "type": "VAE",
          "link": 638
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_AudioVae",
      "properties": {
        "previousName": "AudioVae",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "AudioVae"
      ],
      "color": "#322",
      "bgcolor": "#533",
      "shape": 1
    },
    {
      "id": 341,
      "type": "SetNode",
      "pos": [
        544.8346130565615,
        4902.757291894085
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 103,
      "mode": 0,
      "inputs": [
        {
          "name": "LATENT_UPSCALE_MODEL",
          "type": "LATENT_UPSCALE_MODEL",
          "link": 637
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_UpscaleModel",
      "properties": {
        "previousName": "UpscaleModel",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "UpscaleModel"
      ],
      "shape": 1
    },
    {
      "id": 340,
      "type": "SetNode",
      "pos": [
        551.7589751276541,
        4822.2751262000575
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 102,
      "mode": 0,
      "inputs": [
        {
          "name": "CLIP",
          "type": "CLIP",
          "link": 636
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_LTX_Clip",
      "properties": {
        "previousName": "LTX_Clip",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "LTX_Clip"
      ],
      "color": "#432",
      "bgcolor": "#653",
      "shape": 1
    },
    {
      "id": 403,
      "type": "GetNode",
      "pos": [
        1716.1209385193692,
        5692.0232156676
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 0,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            691
          ]
        }
      ],
      "title": "Get_Nevative1",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Nevative1"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 346,
      "type": "GetNode",
      "pos": [
        1714.1296670418799,
        5733.951125628603
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 1,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "VAE",
          "type": "VAE",
          "links": [
            640
          ]
        }
      ],
      "title": "Get_AudioVae",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "AudioVae"
      ],
      "color": "#322",
      "bgcolor": "#533",
      "shape": 1
    },
    {
      "id": 357,
      "type": "GetNode",
      "pos": [
        1666.890380743607,
        6127.041852765448
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 2,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "LATENT",
          "type": "LATENT",
          "links": [
            649
          ]
        }
      ],
      "title": "Get_denoisedOutput2",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "denoisedOutput2"
      ],
      "color": "#323",
      "bgcolor": "#535",
      "shape": 1
    },
    {
      "id": 339,
      "type": "SetNode",
      "pos": [
        540.396538815671,
        4806.308710451402
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 101,
      "mode": 0,
      "inputs": [
        {
          "name": "VAE",
          "type": "VAE",
          "link": 635
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_VideoVAE",
      "properties": {
        "previousName": "VideoVAE",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "VideoVAE"
      ],
      "color": "#322",
      "bgcolor": "#533",
      "shape": 1
    },
    {
      "id": 385,
      "type": "GetNode",
      "pos": [
        348.32773644078617,
        5326.814065764234
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 3,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            668
          ]
        }
      ],
      "title": "Get_EndTime",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "EndTime"
      ],
      "shape": 1
    },
    {
      "id": 362,
      "type": "GetNode",
      "pos": [
        1703.0376905949931,
        6095.634147576185
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 4,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "VAE",
          "type": "VAE",
          "links": [
            653
          ]
        }
      ],
      "title": "Get_AudioVae",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "AudioVae"
      ],
      "color": "#322",
      "bgcolor": "#533",
      "shape": 1
    },
    {
      "id": 386,
      "type": "GetNode",
      "pos": [
        1678.6445602887495,
        5840.468008448984
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 5,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            972
          ]
        }
      ],
      "title": "Get_TotalSets",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "TotalSets"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 349,
      "type": "GetNode",
      "pos": [
        1706.818900313537,
        5612.858809422282
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 6,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "MODEL",
          "type": "MODEL",
          "links": [
            643
          ]
        }
      ],
      "title": "Get_LTXModel",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "LTXModel"
      ],
      "color": "#223",
      "bgcolor": "#335",
      "shape": 1
    },
    {
      "id": 372,
      "type": "SetNode",
      "pos": [
        1696.1275643146857,
        5755.262326825169
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 129,
      "mode": 0,
      "inputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "link": 669
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_EndTime",
      "properties": {
        "previousName": "EndTime",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "EndTime"
      ],
      "shape": 1
    },
    {
      "id": 413,
      "type": "GetNode",
      "pos": [
        1695.3924811912377,
        5761.866069050583
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 7,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "NOISE",
          "type": "NOISE",
          "links": [
            707
          ]
        }
      ],
      "title": "Get_randomnoise",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "randomnoise"
      ],
      "color": "#2e2e2e",
      "bgcolor": "#242121",
      "shape": 1
    },
    {
      "id": 373,
      "type": "SetNode",
      "pos": [
        1689.8900935832878,
        5795.799903285095
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 130,
      "mode": 0,
      "inputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "link": 671
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_Instructions1",
      "properties": {
        "previousName": "Instructions1",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Instructions1"
      ],
      "shape": 1
    },
    {
      "id": 371,
      "type": "SetNode",
      "pos": [
        1692.2813030067125,
        5866.30667649928
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 131,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 674
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": []
        }
      ],
      "title": "Set_TotalSets",
      "properties": {
        "previousName": "TotalSets",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "TotalSets"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 377,
      "type": "SetNode",
      "pos": [
        1706.4704878025796,
        5901.550727110812
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 136,
      "mode": 0,
      "inputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "link": 703
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_Audio",
      "properties": {
        "previousName": "Audio",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Audio"
      ],
      "shape": 1
    },
    {
      "id": 433,
      "type": "GetNode",
      "pos": [
        1669.4631865011543,
        5903.847631179813
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 8,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "FLOAT",
          "type": "FLOAT",
          "links": []
        }
      ],
      "title": "Get_Scene Duration",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Scene Duration"
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 455,
      "type": "GetNode",
      "pos": [
        1700.8110457919554,
        6104.749173157761
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 9,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "links": [
            737
          ]
        }
      ],
      "title": "Get_audiofile",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "audiofile"
      ],
      "shape": 1
    },
    {
      "id": 402,
      "type": "GetNode",
      "pos": [
        1664.6176440199154,
        5668.145749739683
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 10,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            690
          ]
        }
      ],
      "title": "Get_postive1",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "postive1"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 388,
      "type": "SetNode",
      "pos": [
        2448.404719406226,
        6037.816492054448
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 141,
      "mode": 0,
      "inputs": [
        {
          "name": "VHS_FILENAMES",
          "type": "VHS_FILENAMES",
          "link": 677
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_filenamestrigger",
      "properties": {
        "previousName": "filenamestrigger",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "filenamestrigger"
      ],
      "shape": 1
    },
    {
      "id": 411,
      "type": "GetNode",
      "pos": [
        2425.0144797303305,
        6149.647901163705
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 11,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [
            701
          ]
        }
      ],
      "title": "Get_trimedimage",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "trimedimage"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 435,
      "type": "GetNode",
      "pos": [
        1725.1840589882365,
        5843.017690704744
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 12,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            724
          ]
        }
      ],
      "title": "Get_Width",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Width"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 370,
      "type": "SetNode",
      "pos": [
        1721.2730508246384,
        5760.024459106177
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 128,
      "mode": 0,
      "inputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "link": 666
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_StartTime",
      "properties": {
        "previousName": "StartTime",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "StartTime"
      ],
      "shape": 1
    },
    {
      "id": 553,
      "type": "GetNode",
      "pos": [
        1698.0562534229493,
        5635.599150778343
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 13,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            845
          ]
        }
      ],
      "title": "Get_fixedduratin",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "fixedduratin"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 374,
      "type": "SetNode",
      "pos": [
        1685.4284887825245,
        5903.899025817239
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 132,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 702
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_FramePerScene",
      "properties": {
        "previousName": "FramePerScene",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "FramePerScene"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 347,
      "type": "GetNode",
      "pos": [
        1721.1528311765828,
        5845.302548532469
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 14,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "VAE",
          "type": "VAE",
          "links": [
            641
          ]
        }
      ],
      "title": "Get_VideoVAE",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "VideoVAE"
      ],
      "color": "#322",
      "bgcolor": "#533",
      "shape": 1
    },
    {
      "id": 369,
      "type": "SetNode",
      "pos": [
        1716.088938484459,
        5795.16344887388
      ],
      "size": [
        210,
        59.19181765377289
      ],
      "flags": {
        "collapsed": true
      },
      "order": 127,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 662
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_Index",
      "properties": {
        "previousName": "Index",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Index"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 358,
      "type": "SetNode",
      "pos": [
        1685.535747728763,
        5762.324711187613
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 126,
      "mode": 0,
      "inputs": [
        {
          "name": "LATENT",
          "type": "LATENT",
          "link": 650
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_denoisedOutput",
      "properties": {
        "previousName": "denoisedOutput",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "denoisedOutput"
      ],
      "color": "#323",
      "bgcolor": "#535",
      "shape": 1
    },
    {
      "id": 382,
      "type": "GetNode",
      "pos": [
        466.0276783811063,
        5239.877589458603
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 15,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            954
          ]
        }
      ],
      "title": "Get_Index",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Index"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 387,
      "type": "GetNode",
      "pos": [
        1672.5160882220687,
        5882.317728569784
      ],
      "size": [
        210,
        60.383635307545774
      ],
      "flags": {
        "collapsed": true
      },
      "order": 16,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            973
          ]
        }
      ],
      "title": "Get_OutputFolder",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "OutputFolder"
      ],
      "shape": 1
    },
    {
      "id": 367,
      "type": "GetNode",
      "pos": [
        1714.0826941109385,
        5608.2358888450535
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 17,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": []
        }
      ],
      "title": "Get_image",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "image"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 404,
      "type": "GetNode",
      "pos": [
        326.1415087066685,
        5286.872230508102
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 18,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            953
          ]
        }
      ],
      "title": "Get_OutputFolder",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "OutputFolder"
      ],
      "shape": 1
    },
    {
      "id": 405,
      "type": "GetNode",
      "pos": [
        321.0754464490249,
        5233.882315834612
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 19,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            955
          ]
        }
      ],
      "title": "Get_OverWriteMode",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "OverWriteMode"
      ],
      "shape": 1
    },
    {
      "id": 604,
      "type": "SetNode",
      "pos": [
        1675.5481122198341,
        5633.181534708965
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 140,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 916
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_preframes",
      "properties": {
        "previousName": "preframes",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "preframes"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 390,
      "type": "SetNode",
      "pos": [
        1675.5972094309516,
        5807.830974237387
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 118,
      "mode": 0,
      "inputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "link": 679
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_Condition1",
      "properties": {
        "previousName": "Condition1",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Condition1"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 348,
      "type": "GetNode",
      "pos": [
        1693.507951834063,
        5782.911103682906
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 20,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "CLIP",
          "type": "CLIP",
          "links": [
            642
          ]
        }
      ],
      "title": "Get_LTX_Clip",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "LTX_Clip"
      ],
      "color": "#432",
      "bgcolor": "#653",
      "shape": 1
    },
    {
      "id": 406,
      "type": "SetNode",
      "pos": [
        391.78163802872547,
        5265.584181745849
      ],
      "size": [
        212.16694118867736,
        61.083470594338905
      ],
      "flags": {
        "collapsed": true
      },
      "order": 107,
      "mode": 0,
      "inputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "link": 956
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_OutputPath",
      "properties": {
        "previousName": "OutputPath",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "OutputPath"
      ],
      "shape": 1
    },
    {
      "id": 418,
      "type": "GetNode",
      "pos": [
        1720.2071601584162,
        6275.146713086423
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 21,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "links": [
            712
          ]
        }
      ],
      "title": "Get_audio00",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "audio00"
      ],
      "shape": 1
    },
    {
      "id": 408,
      "type": "SetNode",
      "pos": [
        349.74264847005435,
        5295.278093047079
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 108,
      "mode": 0,
      "inputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "link": 912
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_cropped audio",
      "properties": {
        "previousName": "cropped audio",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "cropped audio"
      ],
      "shape": 1
    },
    {
      "id": 384,
      "type": "GetNode",
      "pos": [
        355.2581796940304,
        5355.379629045962
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 22,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            667
          ]
        }
      ],
      "title": "Get_StartTime",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "StartTime"
      ],
      "shape": 1
    },
    {
      "id": 420,
      "type": "GetNode",
      "pos": [
        376.7146254327832,
        5332.780742476405
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 23,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "links": [
            714
          ]
        }
      ],
      "title": "Get_audiofile",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "audiofile"
      ],
      "shape": 1
    },
    {
      "id": 407,
      "type": "GetNode",
      "pos": [
        2452.5853195676473,
        5929.254714904651
      ],
      "size": [
        210,
        61.06021286361283
      ],
      "flags": {
        "collapsed": true
      },
      "order": 24,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            697
          ]
        }
      ],
      "title": "Get_OutputPath",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "OutputPath"
      ],
      "shape": 1
    },
    {
      "id": 431,
      "type": "SetNode",
      "pos": [
        320.94855021676386,
        5287.8966862313855
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 96,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 1155
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_frames per second",
      "properties": {
        "previousName": "frames per second",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "frames per second"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 430,
      "type": "SetNode",
      "pos": [
        363.4382911765308,
        5327.8240194412365
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 92,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 1151
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_Height",
      "properties": {
        "previousName": "Height",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Height"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 450,
      "type": "SetNode",
      "pos": [
        343.1325868283157,
        5370.257541252979
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 93,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 1152
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_Seed",
      "properties": {
        "previousName": "Seed",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Seed"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 429,
      "type": "SetNode",
      "pos": [
        392.435556992264,
        5316.25411324836
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 91,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 1150
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_Width",
      "properties": {
        "previousName": "Width",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Width"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 297,
      "type": "VRGDG_AudioCrop",
      "pos": [
        321.7235825369019,
        5292.00297668028
      ],
      "size": [
        270,
        82
      ],
      "flags": {
        "collapsed": true
      },
      "order": 74,
      "mode": 0,
      "inputs": [
        {
          "name": "audio",
          "type": "AUDIO",
          "link": 714
        },
        {
          "name": "start_time",
          "type": "STRING",
          "widget": {
            "name": "start_time"
          },
          "link": 667
        },
        {
          "name": "end_time",
          "type": "STRING",
          "widget": {
            "name": "end_time"
          },
          "link": 668
        }
      ],
      "outputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "links": [
            912
          ]
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "0b6d046efe93289ded6c1038cabd33642b602f78",
        "Node name for S&R": "VRGDG_AudioCrop",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "0:00",
        "1:00"
      ],
      "color": "#233",
      "bgcolor": "#355",
      "shape": 1
    },
    {
      "id": 463,
      "type": "GetNode",
      "pos": [
        1689.6872490755716,
        5884.358766225036
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 25,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "links": [
            971
          ]
        }
      ],
      "title": "Get_audiofile",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "audiofile"
      ],
      "shape": 1
    },
    {
      "id": 540,
      "type": "GetNode",
      "pos": [
        1640.7860027156771,
        5912.601188771048
      ],
      "size": [
        211.01040232717878,
        58.98959767282122
      ],
      "flags": {
        "collapsed": true
      },
      "order": 26,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            814
          ]
        }
      ],
      "title": "Get_frames per second",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "frames per second"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 606,
      "type": "GetNode",
      "pos": [
        1713.7502773010985,
        5913.109525844859
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 27,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            918
          ]
        }
      ],
      "title": "Get_Index",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Index"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 423,
      "type": "GetNode",
      "pos": [
        1681.5346496090613,
        5906.73212001627
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 28,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [
            798
          ]
        }
      ],
      "title": "Get_decodedimage",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "decodedimage"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 605,
      "type": "GetNode",
      "pos": [
        1703.854542602555,
        5866.57804610379
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 29,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            917
          ]
        }
      ],
      "title": "Get_preframes",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "preframes"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 410,
      "type": "SetNode",
      "pos": [
        1673.8814701090694,
        5885.9716764952345
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 119,
      "mode": 0,
      "inputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "link": 799
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_trimedimage",
      "properties": {
        "previousName": "trimedimage",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "trimedimage"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 738,
      "type": "VRGDG_ShowText",
      "pos": [
        699.3993476984699,
        5309.19788950015
      ],
      "size": [
        220.7678549503154,
        110.19831178158165
      ],
      "flags": {},
      "order": 99,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "shape": 7,
          "type": "STRING",
          "link": 1158
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "title": "Audio File Path display",
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowText",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "Z:\\ComfyUI\\ComfyUI_windows_portable\\ComfyUI\\output\\VRGDG_AudioFiles\\Whisper in the Dark.mp3"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 359,
      "type": "GetNode",
      "pos": [
        1681.6293149789499,
        5613.457554869318
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 30,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "LATENT",
          "type": "LATENT",
          "links": [
            651
          ]
        }
      ],
      "title": "Get_denoisedOutput",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "denoisedOutput"
      ],
      "color": "#323",
      "bgcolor": "#535",
      "shape": 1
    },
    {
      "id": 631,
      "type": "GetNode",
      "pos": [
        1686.2145077266346,
        5615.991403210249
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 31,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [
            950,
            951
          ]
        }
      ],
      "title": "Get_nanoimage",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "nanoimage"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 397,
      "type": "GetNode",
      "pos": [
        1688.7792181481975,
        5625.446400743747
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 32,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            686
          ]
        }
      ],
      "title": "Get_postive1",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "postive1"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 350,
      "type": "GetNode",
      "pos": [
        1669.7933889773587,
        5629.9568270128075
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 33,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "LATENT_UPSCALE_MODEL",
          "type": "LATENT_UPSCALE_MODEL",
          "links": [
            644
          ]
        }
      ],
      "title": "Get_UpscaleModel",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "UpscaleModel"
      ],
      "shape": 1
    },
    {
      "id": 355,
      "type": "SetNode",
      "pos": [
        1675.8085505765548,
        5648.4369283379
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 109,
      "mode": 0,
      "inputs": [
        {
          "name": "LATENT",
          "type": "LATENT",
          "link": 647
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_denoisedOutput2",
      "properties": {
        "previousName": "denoisedOutput2",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "denoisedOutput2"
      ],
      "color": "#323",
      "bgcolor": "#535",
      "shape": 1
    },
    {
      "id": 366,
      "type": "GetNode",
      "pos": [
        1697.4127230665506,
        5677.753629390699
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 34,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": []
        }
      ],
      "title": "Get_image",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "image"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 398,
      "type": "GetNode",
      "pos": [
        1704.222600715426,
        5696.031301924219
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 35,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            687
          ]
        }
      ],
      "title": "Get_Nevative1",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Nevative1"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 352,
      "type": "GetNode",
      "pos": [
        1686.497492801986,
        5694.841256978925
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 36,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "MODEL",
          "type": "MODEL",
          "links": [
            646
          ]
        }
      ],
      "title": "Get_LTXModel",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "LTXModel"
      ],
      "color": "#223",
      "bgcolor": "#335",
      "shape": 1
    },
    {
      "id": 351,
      "type": "GetNode",
      "pos": [
        1688.053481066158,
        5718.611941343704
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 37,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "VAE",
          "type": "VAE",
          "links": [
            645
          ]
        }
      ],
      "title": "Get_VideoVAE",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "VideoVAE"
      ],
      "color": "#322",
      "bgcolor": "#533",
      "shape": 1
    },
    {
      "id": 181,
      "type": "LTXVConditioning",
      "pos": [
        1683.7497220731793,
        5798.519780518804
      ],
      "size": [
        301.73189836561323,
        132.25004742052352
      ],
      "flags": {
        "collapsed": true
      },
      "order": 81,
      "mode": 0,
      "inputs": [
        {
          "name": "positive",
          "type": "CONDITIONING",
          "link": 682
        },
        {
          "name": "negative",
          "type": "CONDITIONING",
          "link": 683
        },
        {
          "name": "frame_rate",
          "type": "FLOAT",
          "widget": {
            "name": "frame_rate"
          },
          "link": 731
        }
      ],
      "outputs": [
        {
          "name": "positive",
          "type": "CONDITIONING",
          "slot_index": 0,
          "links": [
            684
          ]
        },
        {
          "name": "negative",
          "type": "CONDITIONING",
          "slot_index": 1,
          "links": [
            685
          ]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.3.28",
        "Node name for S&R": "LTXVConditioning",
        "enableTabs": false,
        "tabWidth": 65,
        "tabXOffset": 10,
        "hasSecondTab": false,
        "secondTabText": "Send Back",
        "secondTabOffset": 80,
        "secondTabWidth": 65,
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        24
      ],
      "shape": 1
    },
    {
      "id": 394,
      "type": "GetNode",
      "pos": [
        1682.217508319829,
        5823.323968112342
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 38,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            683
          ]
        }
      ],
      "title": "Get_condition2",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "condition2"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 444,
      "type": "GetNode",
      "pos": [
        1696.683930670207,
        5838.696846358977
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 39,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "FLOAT",
          "type": "FLOAT",
          "links": [
            731
          ]
        }
      ],
      "title": "Get_floatfps",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "floatfps"
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 233,
      "type": "ConditioningZeroOut",
      "pos": [
        1685.2761376806382,
        5927.012746979385
      ],
      "size": [
        292.90757049494823,
        117.73189836561323
      ],
      "flags": {
        "collapsed": true
      },
      "order": 84,
      "mode": 0,
      "inputs": [
        {
          "name": "conditioning",
          "type": "CONDITIONING",
          "link": 680
        }
      ],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            681
          ]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.8.2",
        "Node name for S&R": "ConditioningZeroOut",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [],
      "shape": 1
    },
    {
      "id": 445,
      "type": "GetNode",
      "pos": [
        968.9075623979478,
        5402.398619970058
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 40,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            1192
          ]
        }
      ],
      "title": "Get_FramePerScene",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "FramePerScene"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 761,
      "type": "GetNode",
      "pos": [
        1205.7181116601168,
        5397.102792627829
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 41,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            1193
          ]
        }
      ],
      "title": "Get_Index",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Index"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 383,
      "type": "GetNode",
      "pos": [
        1131.0261570919922,
        5609.174294293828
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 42,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            1194
          ]
        }
      ],
      "title": "Get_Instructions1",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Instructions1"
      ],
      "shape": 1
    },
    {
      "id": 482,
      "type": "MarkdownNote",
      "pos": [
        -8.852612616951546,
        4823.919043516063
      ],
      "size": [
        210,
        112.58147512751657
      ],
      "flags": {
        "collapsed": false
      },
      "order": 43,
      "mode": 0,
      "inputs": [],
      "outputs": [],
      "title": "Models",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "# ➡️➡️➡️ LOAD YOUR MODELS ➡️➡️➡️\n"
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 438,
      "type": "SetNode",
      "pos": [
        355.8516592426245,
        5296.985728545902
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 122,
      "mode": 0,
      "inputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "link": 726
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_foldername",
      "properties": {
        "previousName": "foldername",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "foldername"
      ],
      "shape": 1
    },
    {
      "id": 409,
      "type": "GetNode",
      "pos": [
        2462.960255423286,
        6088.044299746908
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 44,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "links": [
            699
          ]
        }
      ],
      "title": "Get_cropped audio",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "cropped audio"
      ],
      "shape": 1
    },
    {
      "id": 737,
      "type": "VRGDG_ShowText",
      "pos": [
        707.1433696975226,
        5162.394306810345
      ],
      "size": [
        210.19746767237226,
        84.13713002868826
      ],
      "flags": {},
      "order": 98,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "shape": 7,
          "type": "STRING",
          "link": 1157
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "title": "Folder Name display",
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowText",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "Whisper in the Dark"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 552,
      "type": "SetNode",
      "pos": [
        354.84256153975866,
        5274.193892875784
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 100,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 1234
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_fixedduratin",
      "properties": {
        "previousName": "fixedduratin",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "fixedduratin"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 760,
      "type": "VRGDG_ShowAny",
      "pos": [
        970.7061381980171,
        5382.757360209895
      ],
      "size": [
        210,
        88
      ],
      "flags": {},
      "order": 76,
      "mode": 0,
      "inputs": [
        {
          "name": "value",
          "shape": 7,
          "type": "*",
          "link": 1192
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "title": "frames count for this run",
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowAny",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "57"
      ],
      "color": "#432",
      "bgcolor": "#653",
      "shape": 1
    },
    {
      "id": 758,
      "type": "VRGDG_ShowAny",
      "pos": [
        1203.2626594846413,
        5380.2478243916985
      ],
      "size": [
        173.43623965364205,
        81.37759890623875
      ],
      "flags": {},
      "order": 77,
      "mode": 0,
      "inputs": [
        {
          "name": "value",
          "shape": 7,
          "type": "*",
          "link": 1193
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "title": "Current index",
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowAny",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "23"
      ],
      "color": "#432",
      "bgcolor": "#653",
      "shape": 1
    },
    {
      "id": 454,
      "type": "SetNode",
      "pos": [
        341.0169309896198,
        5290.146036953376
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 95,
      "mode": 0,
      "inputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "link": 1154
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_audiofile",
      "properties": {
        "previousName": "audiofile",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "audiofile"
      ],
      "shape": 1
    },
    {
      "id": 437,
      "type": "PrimitiveString",
      "pos": [
        410.1966636069143,
        5265.710742694524
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 94,
      "mode": 0,
      "inputs": [
        {
          "name": "value",
          "type": "STRING",
          "widget": {
            "name": "value"
          },
          "link": 1185
        }
      ],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            726
          ]
        }
      ],
      "title": "FolderName",
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.9.2",
        "Node name for S&R": "PrimitiveString",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        ""
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 634,
      "type": "VRGDG_BuildVideoOutputPath_General_SRT",
      "pos": [
        306.38467066461857,
        5253.150722279534
      ],
      "size": [
        407.9,
        130
      ],
      "flags": {
        "collapsed": true
      },
      "order": 72,
      "mode": 0,
      "inputs": [
        {
          "name": "output_folder",
          "type": "STRING",
          "widget": {
            "name": "output_folder"
          },
          "link": 953
        },
        {
          "name": "chunk_index",
          "type": "INT",
          "widget": {
            "name": "chunk_index"
          },
          "link": 954
        },
        {
          "name": "overwrite_mode",
          "type": "STRING",
          "widget": {
            "name": "overwrite_mode"
          },
          "link": 955
        }
      ],
      "outputs": [
        {
          "name": "output_path",
          "type": "STRING",
          "links": [
            956
          ]
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "0b6d046efe93289ded6c1038cabd33642b602f78",
        "Node name for S&R": "VRGDG_BuildVideoOutputPath_General_SRT",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "",
        0,
        "video",
        ""
      ],
      "color": "#223",
      "bgcolor": "#335",
      "shape": 1
    },
    {
      "id": 794,
      "type": "VRGDG_IntToFloat",
      "pos": [
        347.109123207696,
        5284.396023128456
      ],
      "size": [
        270,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 97,
      "mode": 0,
      "inputs": [
        {
          "name": "value",
          "type": "INT",
          "widget": {
            "name": "value"
          },
          "link": 1237
        }
      ],
      "outputs": [
        {
          "name": "value",
          "type": "FLOAT",
          "links": [
            1238
          ]
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_IntToFloat",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        0
      ],
      "shape": 1
    },
    {
      "id": 443,
      "type": "SetNode",
      "pos": [
        354.8819266480235,
        5259.591328182441
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 123,
      "mode": 0,
      "inputs": [
        {
          "name": "FLOAT",
          "type": "FLOAT",
          "link": 1238
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_floatfps",
      "properties": {
        "previousName": "floatfps",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "floatfps"
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 587,
      "type": "SetNode",
      "pos": [
        631.740884733863,
        5590.387386988052
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 147,
      "mode": 0,
      "inputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "link": 1285
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_prompt",
      "properties": {
        "previousName": "prompt",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "prompt"
      ],
      "shape": 1
    },
    {
      "id": 815,
      "type": "VRGDG_ShowText",
      "pos": [
        623.3243482357217,
        5637.456470363386
      ],
      "size": [
        424.9525005954928,
        244.155566592367
      ],
      "flags": {},
      "order": 146,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "shape": 7,
          "type": "STRING",
          "link": 1279
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowText",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "A blonde woman singing with passion in a dark, moody bedroom during the late night. The subject tilts her head back and clutches her chest, her mouth opening wide as she belts out a soulful melody, her body swaying with emotional intensity and her hands reaching out as if grasping for a lost memory. Her long, flowing blonde hair and the red satin of her dress ripple and flow with her dramatic movements. The camera performs a slow, dramatic push-in toward her face, maintaining a clear medium shot of her expressive features. The environment reacts to her energy as thick, swirling fog drifts through the room, catching the light as it brushes against the fogged mirror and shifts around her silhouette."
      ]
    },
    {
      "id": 586,
      "type": "GetNode",
      "pos": [
        211.54722297134217,
        6456.910508213587
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 45,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            897
          ]
        }
      ],
      "title": "Get_Index",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Index"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 690,
      "type": "PrimitiveInt",
      "pos": [
        1366.9570352259605,
        5623.805806423745
      ],
      "size": [
        270,
        82
      ],
      "flags": {
        "collapsed": true
      },
      "order": 46,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            1079,
            1080
          ]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.10.0",
        "Node name for S&R": "PrimitiveInt",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        450717514388337,
        "randomize"
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 686,
      "type": "VRGDG_LatestSRTAutoLoader",
      "pos": [
        1335.063665009646,
        5592.237879484512
      ],
      "size": [
        249.9,
        102
      ],
      "flags": {},
      "order": 80,
      "mode": 0,
      "inputs": [
        {
          "name": "trigger",
          "type": "INT",
          "widget": {
            "name": "trigger"
          },
          "link": 1079
        },
        {
          "name": "refresh",
          "type": "INT",
          "widget": {
            "name": "refresh"
          },
          "link": 1080
        }
      ],
      "outputs": [
        {
          "name": "srt_full_path",
          "type": "STRING",
          "links": [
            1074,
            1188
          ]
        },
        {
          "name": "srt_file_name",
          "type": "STRING",
          "links": []
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_LatestSRTAutoLoader",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        0,
        0
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 755,
      "type": "VRGDG_ShowText",
      "pos": [
        1348.4147825454447,
        5741.919995310232
      ],
      "size": [
        217.00614550034712,
        109.18324479276816
      ],
      "flags": {},
      "order": 113,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "shape": 7,
          "type": "STRING",
          "link": 1188
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowText",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "Z:\\ComfyUI\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfyui-vrgamedevgirl\\srt_files\\Whisper in the Dark_212.srt"
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 268,
      "type": "10a8d644-7b18-46be-b2d3-53cfa9f21baa",
      "pos": [
        1694.5761240017976,
        6146.457031426429
      ],
      "size": [
        140,
        26
      ],
      "flags": {
        "collapsed": false
      },
      "order": 82,
      "mode": 0,
      "inputs": [
        {
          "name": "anything",
          "type": "*",
          "link": 648
        }
      ],
      "outputs": [],
      "properties": {
        "proxyWidgets": [],
        "cnr_id": "comfy-core",
        "ver": "0.8.2",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [],
      "shape": 1
    },
    {
      "id": 395,
      "type": "SetNode",
      "pos": [
        1710.6382266987084,
        5702.641382680449
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 114,
      "mode": 0,
      "inputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "link": 684
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_postive1",
      "properties": {
        "previousName": "postive1",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "postive1"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 393,
      "type": "GetNode",
      "pos": [
        1689.7456683518299,
        5750.710310856554
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 47,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            682
          ]
        }
      ],
      "title": "Get_Condition1",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Condition1"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 396,
      "type": "SetNode",
      "pos": [
        1693.5162491513813,
        5777.30747921126
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 115,
      "mode": 0,
      "inputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "link": 685
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_Nevative1",
      "properties": {
        "previousName": "Nevative1",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Nevative1"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 356,
      "type": "GetNode",
      "pos": [
        1665.0641434609736,
        5802.436912891885
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 48,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "LATENT",
          "type": "LATENT",
          "links": [
            648
          ]
        }
      ],
      "title": "Get_denoisedOutput2",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "denoisedOutput2"
      ],
      "color": "#323",
      "bgcolor": "#535",
      "shape": 1
    },
    {
      "id": 376,
      "type": "SetNode",
      "pos": [
        1682.5107562086534,
        5798.865699152683
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 135,
      "mode": 0,
      "inputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "link": 693
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_OverWriteMode",
      "properties": {
        "previousName": "OverWriteMode",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "OverWriteMode"
      ],
      "shape": 1
    },
    {
      "id": 451,
      "type": "GetNode",
      "pos": [
        1696.287804283748,
        5828.2023900011845
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 49,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            735
          ]
        }
      ],
      "title": "Get_Seed",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Seed"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 391,
      "type": "GetNode",
      "pos": [
        1706.693130661726,
        5808.84195510622
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 50,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            680
          ]
        }
      ],
      "title": "Get_Condition1",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Condition1"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 412,
      "type": "SetNode",
      "pos": [
        1687.6185983859727,
        5846.137132792323
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 116,
      "mode": 0,
      "inputs": [
        {
          "name": "NOISE",
          "type": "NOISE",
          "link": 706
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_randomnoise",
      "properties": {
        "previousName": "randomnoise",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "randomnoise"
      ],
      "color": "#2e2e2e",
      "bgcolor": "#242121",
      "shape": 1
    },
    {
      "id": 588,
      "type": "GetNode",
      "pos": [
        1710.5769173082313,
        5826.424347026425
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 51,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            900
          ]
        }
      ],
      "title": "Get_prompt",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "prompt"
      ],
      "shape": 1
    },
    {
      "id": 422,
      "type": "SetNode",
      "pos": [
        1692.0277722880242,
        5808.588834602316
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 120,
      "mode": 0,
      "inputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "link": 716
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_decodedimage",
      "properties": {
        "previousName": "decodedimage",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "decodedimage"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 439,
      "type": "GetNode",
      "pos": [
        1698.4098689739644,
        5817.009405677271
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 52,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            727
          ]
        }
      ],
      "title": "Get_foldername",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "foldername"
      ],
      "shape": 1
    },
    {
      "id": 389,
      "type": "GetNode",
      "pos": [
        1682.200054818349,
        5814.940619805516
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 53,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "VHS_FILENAMES",
          "type": "VHS_FILENAMES",
          "links": [
            970
          ]
        }
      ],
      "title": "Get_filenamestrigger",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "filenamestrigger"
      ],
      "shape": 1
    },
    {
      "id": 231,
      "type": "CLIPTextEncode",
      "pos": [
        1673.2531529384546,
        5832.740879031023
      ],
      "size": [
        296.57060976456205,
        201.4538310734497
      ],
      "flags": {
        "collapsed": true
      },
      "order": 85,
      "mode": 0,
      "inputs": [
        {
          "name": "clip",
          "type": "CLIP",
          "link": 642
        },
        {
          "name": "text",
          "type": "STRING",
          "widget": {
            "name": "text"
          },
          "link": 900
        }
      ],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            679
          ]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.8.2",
        "Node name for S&R": "CLIPTextEncode",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "the women speaks"
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 375,
      "type": "SetNode",
      "pos": [
        1678.7076134226113,
        5862.807651267189
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 133,
      "mode": 0,
      "inputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "link": 675
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_OutputFolder",
      "properties": {
        "previousName": "OutputFolder",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "OutputFolder"
      ],
      "shape": 1
    },
    {
      "id": 434,
      "type": "GetNode",
      "pos": [
        1677.6904648547375,
        5878.660815961494
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 54,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            723
          ]
        }
      ],
      "title": "Get_frames per second",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "frames per second"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 392,
      "type": "SetNode",
      "pos": [
        1711.2651353398667,
        5878.6579716185315
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 117,
      "mode": 0,
      "inputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "link": 681
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_condition2",
      "properties": {
        "previousName": "condition2",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "condition2"
      ],
      "color": "#332922",
      "bgcolor": "#593930",
      "shape": 1
    },
    {
      "id": 378,
      "type": "SetNode",
      "pos": [
        1678.73081320637,
        5864.264130879103
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 138,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 704
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_framesForLtx",
      "properties": {
        "previousName": "framesForLtx",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "framesForLtx"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 269,
      "type": "acbce015-ba7f-49d9-9d32-4a29c248e609",
      "pos": [
        1709.5151462538186,
        5913.021081801383
      ],
      "size": [
        140,
        26
      ],
      "flags": {},
      "order": 87,
      "mode": 0,
      "inputs": [
        {
          "name": "anything",
          "type": "*",
          "link": 652
        }
      ],
      "outputs": [],
      "properties": {
        "proxyWidgets": [],
        "cnr_id": "comfy-core",
        "ver": "0.8.2",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [],
      "shape": 1
    },
    {
      "id": 360,
      "type": "SetNode",
      "pos": [
        1686.565190390286,
        5858.821017402511
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 55,
      "mode": 0,
      "inputs": [
        {
          "name": "*",
          "type": "*",
          "link": null
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": [
            652
          ]
        }
      ],
      "title": "Set_denoisedOutput",
      "properties": {
        "previousName": "",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "denoisedOutput_0"
      ],
      "color": "#323",
      "bgcolor": "#535",
      "shape": 1
    },
    {
      "id": 417,
      "type": "SetNode",
      "pos": [
        1707.9255504945384,
        5872.937761784651
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 137,
      "mode": 0,
      "inputs": [
        {
          "name": "AUDIO",
          "type": "AUDIO",
          "link": 711
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_audio00",
      "properties": {
        "previousName": "audio00",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "audio00"
      ],
      "shape": 1
    },
    {
      "id": 379,
      "type": "SetNode",
      "pos": [
        1687.1448858798403,
        5894.167110435982
      ],
      "size": [
        210,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 139,
      "mode": 0,
      "inputs": [
        {
          "name": "INT",
          "type": "INT",
          "link": 705
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_PreRollFrames",
      "properties": {
        "previousName": "PreRollFrames",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "PreRollFrames"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 436,
      "type": "GetNode",
      "pos": [
        1708.1948294103083,
        5910.040429502815
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 56,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            725
          ]
        }
      ],
      "title": "Get_Height",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "Height"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 235,
      "type": "RandomNoise",
      "pos": [
        1695.8626297717328,
        5922.536691439396
      ],
      "size": [
        224.85687660390568,
        82.9863644985553
      ],
      "flags": {
        "collapsed": true
      },
      "order": 83,
      "mode": 0,
      "inputs": [
        {
          "name": "noise_seed",
          "type": "INT",
          "widget": {
            "name": "noise_seed"
          },
          "link": 735
        }
      ],
      "outputs": [
        {
          "name": "NOISE",
          "type": "NOISE",
          "links": [
            706
          ]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.8.2",
        "Node name for S&R": "RandomNoise",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        36164627960122,
        "fixed"
      ],
      "shape": 1
    },
    {
      "id": 414,
      "type": "GetNode",
      "pos": [
        1692.7671483782735,
        5948.759436022585
      ],
      "size": [
        210,
        50
      ],
      "flags": {
        "collapsed": true
      },
      "order": 57,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            797
          ]
        }
      ],
      "title": "Get_FramePerScene",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "FramePerScene"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 530,
      "type": "VRGDG_TrimImageBatch_SRTOnly",
      "pos": [
        1652.3941533579086,
        5953.936677147287
      ],
      "size": [
        323.9,
        130
      ],
      "flags": {
        "collapsed": true
      },
      "order": 88,
      "mode": 0,
      "inputs": [
        {
          "name": "images",
          "type": "IMAGE",
          "link": 798
        },
        {
          "name": "frames_per_scene",
          "type": "INT",
          "widget": {
            "name": "frames_per_scene"
          },
          "link": 797
        },
        {
          "name": "pre_frames",
          "type": "INT",
          "widget": {
            "name": "pre_frames"
          },
          "link": 917
        },
        {
          "name": "chunk_index",
          "type": "INT",
          "widget": {
            "name": "chunk_index"
          },
          "link": 918
        },
        {
          "name": "fps",
          "type": "INT",
          "widget": {
            "name": "fps"
          },
          "link": 814
        }
      ],
      "outputs": [
        {
          "name": "images",
          "type": "IMAGE",
          "links": [
            799
          ]
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "0b6d046efe93289ded6c1038cabd33642b602f78",
        "Node name for S&R": "VRGDG_TrimImageBatch_SRTOnly",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        0,
        0,
        239,
        25
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 361,
      "type": "GetNode",
      "pos": [
        1691.7251514446368,
        5983.934043011127
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 58,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "VAE",
          "type": "VAE",
          "links": [
            654
          ]
        }
      ],
      "title": "Get_VideoVAE",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "VideoVAE"
      ],
      "color": "#322",
      "bgcolor": "#533",
      "shape": 1
    },
    {
      "id": 609,
      "type": "MarkdownNote",
      "pos": [
        2002.0206797681774,
        6180.9676045596225
      ],
      "size": [
        210,
        194.98921653708294
      ],
      "flags": {},
      "order": 59,
      "mode": 0,
      "inputs": [],
      "outputs": [],
      "title": "Remake mode",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "# Move bad clips to remake folder\n\nAt the end of the run, you can move clips you don't like to the remake folder. Then turn on \"use remake folder\" and hit run. It will remake the clips for you. If you do this more than once make sure to delete any temp files from the folder first. "
      ],
      "color": "#432",
      "bgcolor": "#653",
      "shape": 1
    },
    {
      "id": 740,
      "type": "MarkdownNote",
      "pos": [
        1992.8917123875772,
        5988.855727277979
      ],
      "size": [
        210,
        149.76830839614922
      ],
      "flags": {},
      "order": 60,
      "mode": 0,
      "inputs": [],
      "outputs": [],
      "title": "note",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "# Tail loss and pre frames\n\nThese are warm up and warm down frames. This helps keeps things continuous. Default settings work best."
      ],
      "color": "#432",
      "bgcolor": "#653",
      "shape": 1
    },
    {
      "id": 236,
      "type": "f9b0e4a7-3741-45ee-adfd-065c755d6f56",
      "pos": [
        2034.1921598483445,
        5843.45030807602
      ],
      "size": [
        140,
        66
      ],
      "flags": {
        "collapsed": false
      },
      "order": 89,
      "mode": 0,
      "inputs": [
        {
          "name": "av_latent",
          "type": "LATENT",
          "link": 649
        },
        {
          "name": "audio_vae",
          "type": "VAE",
          "link": 653
        },
        {
          "name": "vae",
          "type": "VAE",
          "link": 654
        }
      ],
      "outputs": [
        {
          "name": "Audio",
          "type": "AUDIO",
          "links": []
        },
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [
            716
          ]
        }
      ],
      "properties": {
        "proxyWidgets": [],
        "cnr_id": "comfy-core",
        "ver": "0.8.2",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 219,
      "type": "f90e476f-2a4f-488c-89f7-e7f2417460dc",
      "pos": [
        1997.001822345835,
        5601.844586201371
      ],
      "size": [
        221,
        178
      ],
      "flags": {
        "collapsed": false
      },
      "order": 75,
      "mode": 0,
      "inputs": [
        {
          "name": "model",
          "type": "MODEL",
          "link": 646
        },
        {
          "name": "positive",
          "type": "CONDITIONING",
          "link": 686
        },
        {
          "name": "negative",
          "type": "CONDITIONING",
          "link": 687
        },
        {
          "name": "upscale_model",
          "type": "LATENT_UPSCALE_MODEL",
          "link": 644
        },
        {
          "name": "vae",
          "type": "VAE",
          "link": 645
        },
        {
          "name": "image",
          "type": "IMAGE",
          "link": 951
        },
        {
          "label": "bypass image",
          "name": "bypass",
          "type": "BOOLEAN",
          "widget": {
            "name": "bypass"
          },
          "link": null
        },
        {
          "name": "av_latent",
          "type": "LATENT",
          "link": 651
        }
      ],
      "outputs": [
        {
          "name": "denoised_output",
          "type": "LATENT",
          "links": [
            647
          ]
        }
      ],
      "properties": {
        "proxyWidgets": [
          [
            "-1",
            "bypass"
          ]
        ],
        "cnr_id": "comfy-core",
        "ver": "0.8.2",
        "ue_properties": {
          "widget_ue_connectable": {
            "bypass": true
          },
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        false
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 537,
      "type": "GetNode",
      "pos": [
        2577.295490560371,
        5869.359963604857
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": true
      },
      "order": 61,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "INT",
          "type": "INT",
          "links": [
            1239
          ]
        }
      ],
      "title": "Get_frames per second",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "frames per second"
      ],
      "color": "#1b4669",
      "bgcolor": "#29699c",
      "shape": 1
    },
    {
      "id": 795,
      "type": "VRGDG_IntToFloat",
      "pos": [
        2603.025380134187,
        5898.646097971311
      ],
      "size": [
        270,
        58
      ],
      "flags": {
        "collapsed": true
      },
      "order": 90,
      "mode": 0,
      "inputs": [
        {
          "name": "value",
          "type": "INT",
          "widget": {
            "name": "value"
          },
          "link": 1239
        }
      ],
      "outputs": [
        {
          "name": "value",
          "type": "FLOAT",
          "links": [
            1240
          ]
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_IntToFloat",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        0
      ],
      "shape": 1
    },
    {
      "id": 768,
      "type": "Reroute",
      "pos": [
        1190.6346207318793,
        5995.946244088235
      ],
      "size": [
        82,
        26
      ],
      "flags": {},
      "order": 148,
      "mode": 0,
      "inputs": [
        {
          "name": "",
          "type": "*",
          "link": 1249
        }
      ],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [
            1206
          ]
        }
      ],
      "properties": {
        "showOutputText": true,
        "horizontal": false,
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 630,
      "type": "SetNode",
      "pos": [
        1327.4859824771304,
        6020.324118459145
      ],
      "size": [
        210,
        61.310999419149994
      ],
      "flags": {
        "collapsed": true
      },
      "order": 149,
      "mode": 0,
      "inputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "link": 1206
        }
      ],
      "outputs": [
        {
          "name": "*",
          "type": "*",
          "links": null
        }
      ],
      "title": "Set_nanoimage",
      "properties": {
        "previousName": "nanoimage",
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "nanoimage"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 736,
      "type": "be185d6e-1771-4b9a-a682-a726b24d06e2",
      "pos": [
        240.22323742949567,
        5151.007829046496
      ],
      "size": [
        418.4084562138544,
        323.8377143558346
      ],
      "flags": {},
      "order": 62,
      "mode": 0,
      "inputs": [
        {
          "label": "Frames Per Second",
          "name": "value",
          "type": "INT",
          "widget": {
            "name": "value"
          },
          "link": null
        },
        {
          "label": "Width",
          "name": "value_1",
          "type": "INT",
          "widget": {
            "name": "value_1"
          },
          "link": null
        },
        {
          "label": "Height",
          "name": "value_2",
          "type": "INT",
          "widget": {
            "name": "value_2"
          },
          "link": null
        },
        {
          "label": "Seed",
          "name": "value_3",
          "type": "INT",
          "widget": {
            "name": "value_3"
          },
          "link": null
        },
        {
          "label": "Scene Duration when fixed",
          "name": "value_4",
          "type": "INT",
          "widget": {
            "name": "value_4"
          },
          "link": null
        }
      ],
      "outputs": [
        {
          "label": "width",
          "name": "INT_1",
          "type": "INT",
          "links": [
            1150
          ]
        },
        {
          "label": "height",
          "name": "INT_2",
          "type": "INT",
          "links": [
            1151
          ]
        },
        {
          "label": "seed",
          "name": "INT_3",
          "type": "INT",
          "links": [
            1152
          ]
        },
        {
          "label": "for folder name",
          "name": "result_text",
          "type": "STRING",
          "links": [
            1185
          ]
        },
        {
          "name": "audio",
          "type": "AUDIO",
          "links": [
            1154
          ]
        },
        {
          "label": "frames per second",
          "name": "INT_4",
          "type": "INT",
          "links": [
            1155,
            1237
          ]
        },
        {
          "label": "Folder Name",
          "name": "STRING",
          "type": "STRING",
          "links": [
            1157
          ]
        },
        {
          "label": "Audio File Path",
          "name": "STRING_1",
          "type": "STRING",
          "links": [
            1158
          ]
        },
        {
          "label": "SceneDurationWhenFixed",
          "name": "INT",
          "type": "INT",
          "links": [
            1234
          ]
        }
      ],
      "properties": {
        "proxyWidgets": [
          [
            "-1",
            "value"
          ],
          [
            "-1",
            "value_1"
          ],
          [
            "-1",
            "value_2"
          ],
          [
            "-1",
            "value_3"
          ],
          [
            "-1",
            "value_4"
          ]
        ],
        "cnr_id": "comfy-core",
        "ver": "0.10.0",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        24,
        1920,
        1080,
        123456789,
        0
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 817,
      "type": "VRGDG_LoadTextAdvanced",
      "pos": [
        -61.944283699118834,
        6249.333995365253
      ],
      "size": [
        227,
        174
      ],
      "flags": {},
      "order": 63,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "text",
          "type": "STRING",
          "links": [
            1290
          ]
        },
        {
          "name": "file_path",
          "type": "STRING",
          "links": null
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_LoadTextAdvanced",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "themestyle",
        true,
        "themestyle.txt",
        "",
        null
      ]
    },
    {
      "id": 762,
      "type": "VRGDG_ShowText",
      "pos": [
        1078.2261245183697,
        5613.167152866716
      ],
      "size": [
        236.05945447602554,
        133.61713387445707
      ],
      "flags": {},
      "order": 78,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "shape": 7,
          "type": "STRING",
          "link": 1194
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "title": "READ ME",
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowText",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "🎬 SRT MODE\nRendering chunk 24 / 24\nOutput folder: Whisper in the Dark_2026-04-27_09-28-25"
      ],
      "color": "#322",
      "bgcolor": "#533",
      "shape": 1
    },
    {
      "id": 770,
      "type": "GetNode",
      "pos": [
        1872.5759981252218,
        6653.604558577403
      ],
      "size": [
        210,
        60
      ],
      "flags": {
        "collapsed": false
      },
      "order": 64,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [
            1205
          ]
        }
      ],
      "title": "Get_nanoimage",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "nanoimage"
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 635,
      "type": "StringConcatenate",
      "pos": [
        1912.949795833428,
        6582.549633353119
      ],
      "size": [
        397.55791751839524,
        203.256109975473
      ],
      "flags": {
        "collapsed": true
      },
      "order": 134,
      "mode": 0,
      "inputs": [
        {
          "name": "string_a",
          "type": "STRING",
          "widget": {
            "name": "string_a"
          },
          "link": 957
        }
      ],
      "outputs": [
        {
          "name": "STRING",
          "type": "STRING",
          "links": [
            958
          ]
        }
      ],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.10.0",
        "Node name for S&R": "StringConcatenate",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "",
        "z-image\\images",
        "\\"
      ],
      "shape": 1
    },
    {
      "id": 632,
      "type": "SaveImage",
      "pos": [
        1670.1036721567843,
        6502.935181978942
      ],
      "size": [
        589.2922185468112,
        401.85025438117464
      ],
      "flags": {},
      "order": 145,
      "mode": 0,
      "inputs": [
        {
          "name": "images",
          "type": "IMAGE",
          "link": 1205
        },
        {
          "name": "filename_prefix",
          "type": "STRING",
          "widget": {
            "name": "filename_prefix"
          },
          "link": 958
        }
      ],
      "outputs": [],
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.10.0",
        "Node name for S&R": "SaveImage",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "justmeagain\\image"
      ],
      "color": "#223",
      "bgcolor": "#335",
      "shape": 1
    },
    {
      "id": 810,
      "type": "VRGDG_ShowText",
      "pos": [
        1113.7217188920508,
        6385.736221283464
      ],
      "size": [
        461.1576263371078,
        280.23443765442244
      ],
      "flags": {},
      "order": 142,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "shape": 7,
          "type": "STRING",
          "link": 1270
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowText",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "A high resolution cinematic photograph of a blonde woman, facing the end with a calm and resigned expression, in a dark bedroom with encroaching shadows and a fogged mirror, during the late night. The subject is wearing a red satin dress, elegant silk accessories, and subtle, fine jewelry. Her hair is blonde, long and flowing, with a soft, smooth texture. The environment is a dark, moody bedroom with heavy shadows and a large, fogged mirror reflecting a hazy, dreamlike space, with deep crimson and charcoal color grading, and soft, diffused light filtering through the mist. Camera is a medium shot with a 50mm prime lens. The weather is still, with a thick, swirling fog, creating a cinematic and surreal mood."
      ]
    },
    {
      "id": 218,
      "type": "5548df69-fe42-439c-993d-20f06190baa7",
      "pos": [
        1640.0185765449596,
        5591.241218231894
      ],
      "size": [
        277.9229346619052,
        629.0829834285987
      ],
      "flags": {
        "collapsed": false
      },
      "order": 112,
      "mode": 0,
      "inputs": [
        {
          "name": "model",
          "type": "MODEL",
          "link": 643
        },
        {
          "name": "positive",
          "type": "CONDITIONING",
          "link": 690
        },
        {
          "name": "negative",
          "type": "CONDITIONING",
          "link": 691
        },
        {
          "name": "vae",
          "type": "VAE",
          "link": 641
        },
        {
          "name": "audio_vae",
          "type": "VAE",
          "link": 640
        },
        {
          "name": "width",
          "type": "INT",
          "widget": {
            "name": "width"
          },
          "link": 724
        },
        {
          "name": "height",
          "type": "INT",
          "widget": {
            "name": "height"
          },
          "link": 725
        },
        {
          "name": "image",
          "type": "IMAGE",
          "link": 950
        },
        {
          "name": "noise",
          "type": "NOISE",
          "link": 707
        },
        {
          "name": "folder_path",
          "type": "STRING",
          "widget": {
            "name": "folder_path"
          },
          "link": 727
        },
        {
          "name": "fps",
          "type": "INT",
          "widget": {
            "name": "fps"
          },
          "link": 723
        },
        {
          "name": "audio",
          "type": "AUDIO",
          "link": 737
        },
        {
          "label": "Mel-band Former",
          "name": "model_name",
          "type": "COMBO",
          "link": null
        },
        {
          "name": "srt_file",
          "type": "STRING",
          "widget": {
            "name": "srt_file"
          },
          "link": 1074
        },
        {
          "name": "fixed_duration",
          "type": "INT",
          "widget": {
            "name": "fixed_duration"
          },
          "link": 845
        }
      ],
      "outputs": [
        {
          "name": "denoised_output",
          "type": "LATENT",
          "links": [
            650
          ]
        },
        {
          "name": "total_duration",
          "type": "FLOAT",
          "links": []
        },
        {
          "name": "index",
          "type": "INT",
          "links": [
            662
          ]
        },
        {
          "name": "start_time",
          "type": "STRING",
          "links": [
            666
          ]
        },
        {
          "name": "end_time",
          "type": "STRING",
          "links": [
            669
          ]
        },
        {
          "name": "instructions",
          "type": "STRING",
          "links": [
            671
          ]
        },
        {
          "name": "total_sets",
          "type": "INT",
          "links": [
            674
          ]
        },
        {
          "name": "frames_per_scene",
          "type": "INT",
          "links": [
            702
          ]
        },
        {
          "name": "output_folder",
          "type": "STRING",
          "links": [
            675,
            957
          ]
        },
        {
          "name": "overwrite_mode",
          "type": "STRING",
          "links": [
            693
          ]
        },
        {
          "name": "audio_1",
          "type": "AUDIO",
          "links": [
            703,
            711
          ]
        },
        {
          "name": "frames_for_ltx",
          "type": "INT",
          "links": [
            704
          ]
        },
        {
          "name": "preroll_frames",
          "type": "INT",
          "links": [
            705,
            916
          ]
        }
      ],
      "properties": {
        "proxyWidgets": [
          [
            "-1",
            "folder_path"
          ],
          [
            "-1",
            "srt_file"
          ],
          [
            "-1",
            "enable_auto_queue_1"
          ],
          [
            "-1",
            "redo_prompt_number"
          ],
          [
            "-1",
            "overwrite_mode"
          ],
          [
            "-1",
            "tail_loss_frames"
          ],
          [
            "-1",
            "pre_frames"
          ],
          [
            "-1",
            "width"
          ],
          [
            "-1",
            "height"
          ],
          [
            "-1",
            "fps"
          ],
          [
            "-1",
            "fixed_duration"
          ],
          [
            "-1",
            "use_remake_folder"
          ]
        ],
        "cnr_id": "comfy-core",
        "ver": "0.8.2",
        "ue_properties": {
          "widget_ue_connectable": {
            "value": true,
            "bypass": true,
            "upload": true,
            "audioUI": true
          },
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        24,
        "",
        true,
        0,
        "backup",
        25,
        50,
        736,
        416,
        24,
        24,
        false
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 640,
      "type": "VRGDG_CreateFinalVideo_SRT",
      "pos": [
        2527.522759484336,
        5600.812070065183
      ],
      "size": [
        298.9,
        126
      ],
      "flags": {
        "collapsed": true
      },
      "order": 86,
      "mode": 0,
      "inputs": [
        {
          "name": "trigger",
          "type": "VHS_FILENAMES",
          "link": 970
        },
        {
          "name": "audio",
          "type": "AUDIO",
          "link": 971
        },
        {
          "name": "threshold",
          "type": "INT",
          "widget": {
            "name": "threshold"
          },
          "link": 972
        },
        {
          "name": "video_folder",
          "type": "STRING",
          "widget": {
            "name": "video_folder"
          },
          "link": 973
        }
      ],
      "outputs": [],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_CreateFinalVideo_SRT",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        3,
        "-1",
        "video_output"
      ],
      "color": "#223",
      "bgcolor": "#335",
      "shape": 1
    },
    {
      "id": 311,
      "type": "PreviewAudio",
      "pos": [
        1651.1254676136793,
        6274.111338897668
      ],
      "size": [
        255.88497967024614,
        116.29259865699078
      ],
      "flags": {
        "collapsed": false
      },
      "order": 73,
      "mode": 0,
      "inputs": [
        {
          "name": "audio",
          "type": "AUDIO",
          "link": 712
        }
      ],
      "outputs": [],
      "title": "Preview Audio for this run",
      "properties": {
        "cnr_id": "comfy-core",
        "ver": "0.9.2",
        "Node name for S&R": "PreviewAudio",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [],
      "color": "#432",
      "bgcolor": "#653",
      "shape": 1
    },
    {
      "id": 271,
      "type": "7ab38c03-20ca-4807-90e3-a779e4478032",
      "pos": [
        260.91771553344074,
        4749.114180003866
      ],
      "size": [
        688.184654553752,
        291.3688772383912
      ],
      "flags": {},
      "order": 65,
      "mode": 0,
      "inputs": [
        {
          "label": "Unet Loader (GGUF)",
          "name": "unet_name",
          "type": "COMBO",
          "widget": {
            "name": "unet_name"
          },
          "link": null
        },
        {
          "label": "Video-VAELoader KJ Vae_name",
          "name": "vae_name",
          "type": "COMBO",
          "widget": {
            "name": "vae_name"
          },
          "link": null
        },
        {
          "label": "DualClipLoader (GGUF) clip name1",
          "name": "clip_name1",
          "type": "COMBO",
          "widget": {
            "name": "clip_name1"
          },
          "link": null
        },
        {
          "label": "DualClipLoader (GGUF) Clip name 2",
          "name": "clip_name2",
          "type": "COMBO",
          "widget": {
            "name": "clip_name2"
          },
          "link": null
        },
        {
          "label": "Load Latent Upscaler Model name",
          "name": "model_name",
          "type": "COMBO",
          "widget": {
            "name": "model_name"
          },
          "link": null
        },
        {
          "label": "Audio-VAE Loader KJ vae name",
          "name": "vae_name_1",
          "type": "COMBO",
          "widget": {
            "name": "vae_name_1"
          },
          "link": null
        }
      ],
      "outputs": [
        {
          "name": "VAE",
          "type": "VAE",
          "links": [
            635
          ]
        },
        {
          "name": "CLIP",
          "type": "CLIP",
          "links": [
            636
          ]
        },
        {
          "name": "LATENT_UPSCALE_MODEL",
          "type": "LATENT_UPSCALE_MODEL",
          "links": [
            637
          ]
        },
        {
          "label": "Audio_VAE",
          "name": "VAE_1",
          "type": "VAE",
          "links": [
            638
          ]
        },
        {
          "name": "MODEL",
          "type": "MODEL",
          "links": [
            639
          ]
        }
      ],
      "properties": {
        "proxyWidgets": [
          [
            "-1",
            "unet_name"
          ],
          [
            "-1",
            "vae_name"
          ],
          [
            "-1",
            "clip_name1"
          ],
          [
            "-1",
            "clip_name2"
          ],
          [
            "-1",
            "model_name"
          ],
          [
            "-1",
            "vae_name_1"
          ]
        ],
        "cnr_id": "comfy-core",
        "ver": "0.9.2",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "LTX-2.3-22B-distilled-1.1-Q6_K.gguf",
        "LTX23_video_vae_bf16.safetensors",
        "gemma-3-12b-it-abliterated-sikaworld-high-fidelity-edition.safetensors",
        "ltx-2.3_text_projection_bf16.safetensors",
        "ltx-2.3-spatial-upscaler-x2-1.1.safetensors",
        "LTX23_audio_vae_bf16.safetensors"
      ],
      "color": "#323",
      "bgcolor": "#535",
      "shape": 1
    },
    {
      "id": 543,
      "type": "VRGDG_PromptSplitter_General",
      "pos": [
        190.90161148301084,
        5987.069553795357
      ],
      "size": [
        335.9,
        372.1616562079362
      ],
      "flags": {
        "collapsed": false
      },
      "order": 79,
      "mode": 0,
      "inputs": [
        {
          "name": "index",
          "type": "INT",
          "widget": {
            "name": "index"
          },
          "link": 897
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "type": "STRING",
          "links": [
            1265,
            1274
          ]
        }
      ],
      "title": "VRGDG_PromptSplitter_General-LTX prompts",
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "0b6d046efe93289ded6c1038cabd33642b602f78",
        "Node name for S&R": "VRGDG_PromptSplitter_General",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "{\n  \"Prompt1\": \"A female with blonde hair wearing a red satin style satin dress, pressing a finger to her lips to keep silence in a dark cinematic bedroom, with a quiet and mysterious expression, surrounded by moving shadows and soft blue moonlight, creating a mysterious atmosphere.\",\n  \"Prompt2\": \"A female with blonde hair wearing a red satin style satin dress, standing amidst shifting shadows in a dark bedroom, with a melancholic expression, surrounded by dark moving shapes, creating an eerie atmosphere.\",\n  \"Prompt3\": \"A female with blonde hair wearing a red satin style satin dress, reaching for a flickering bathroom light in a dim bathroom, with a cold and trembling expression, surrounded by dim light and shadows, creating a chilling atmosphere.\",\n  \"Prompt4\": \"A female with blonde hair wearing a red satin style satin dress, staring at a steam-covered mirror in a dim bathroom, with a fractured and hollow expression, surrounded by swirling fog and a name appearing in the steam, creating a surreal atmosphere.\",\n  \"Prompt5\": \"A female with blonde hair wearing a red satin style satin dress, drifting like a phantom in a dim bathroom, with a lost and hollow expression, surrounded by thick steam and swirling mist, creating a dreamlike atmosphere.\",\n  \"Prompt6\": \"A female with blonde hair wearing a red satin style satin dress, smiling while tears fall in a dim bathroom, with a forced and breaking expression, surrounded by flickering light and steam, creating a tragic atmosphere.\",\n  \"Prompt7\": \"A female with blondely hair wearing a red satin style satin dress, walking invisibly through a crowded night city street, with a silent and stoic expression, surrounded by blurred pedestrians and bending streetlights, creating a lonely atmosphere.\",\n  \"Prompt8\": \"A female with blonde hair wearing a red satin style satin dress, feeling a phantom presence under her skin in a night city street, with a haunted expression, surrounded by stretching shadows and city lights, creating a restless atmosphere.\",\n  \"Prompt9\": \"A female with blonde hair wearing a red satin style satin dress, falling apart into fragments in a dark hallway, with a crumbling and sorrowful expression, surrounded by dark shadows and swirling particles, creating a dramatic atmosphere.\",\n  \"Prompt10\": \"A female with blonde hair wearing a red satin style satin dress, becoming a faint whisper in the dark hallway, with a ghostly and ethereal expression, surrounded by deep shadows and dim light, creating a haunting atmosphere.\",\n  \"Prompt11\": \"A female with blonde hair wearing a red satin style satin dress, disappearing into thin air in a dark hallway, with a vanishing and spectral expression, surrounded by swirling black smoke and fading light, creating a ghostly atmosphere.\",\n  \"Prompt12\": \"A female with blonde hair wearing a redly satin style satin dress, leaving no physical mark in a dark hallway, with a wispy and translucent expression, surrounded by floating particles and dark voids, creating a surreal atmosphere.\",\n  \"Prompt13\": \"A female with blonde hair wearing a red satin style satin dress, floating as a whisper in the dark hallway, with a soft and ethereal expression, surrounded by swirling shadows and dim light, creating a mysterious atmosphere.\",\n  \"Prompt14\": \"A female with blonde hair wearing a red satin style satin dress, sitting on the bedroom floor in a dark bedroom, with a heavy and weary expression, surrounded by the dark fabric of the dress and moonlight, creating a somber atmosphere.\",\n  \"Prompt15\": \"A female with blonde hair wearing a red satin style satin dress, looking at her hands in a dark bedroom, with a distrustful and lost expression, surrounded by pulsing walls and deep shadows, creating a tense atmosphere.\",\n  \"Prompt16\": \"A female with blonde hair wearing a red satin style satin dress, clutching her secrets in a dark bedroom, with a burdened and heavy expression, surrounded by shadows written on the ceiling, creating a haunted atmosphere.\",\n  \"Prompt17\": \"A female with blonde hair wearing a red satin style satin dress, listening to whispers while awake in a dark bedroom, with a wide-eyed and sleepless expression, surrounded by pulsing walls and moonlight, creating a restless atmosphere.\",\n  \"Prompt18\": \"A female with blonde hair wearing a red satin style satin dress, shedding a single tear amidst a spark of light in a dark bedroom, with a breaking and luminous expression, surrounded by glowing particles and shadows, creating a dramatic atmosphere.\",\n  \"Prompt19\": \"A female with blonde hair wearing a red satin style satin dress, dissolving into a whisper in the dark bedroom, with a fading and ethereal expression, surrounded by swirling shadows and moonlight, creating a ghostly atmosphere.\",\n  \"Prompt20\": \"A female with blonde hair wearing a red satin style satin dress, leaving a ghost beside an ear in a dark bedroom, with a spectral and vanishing expression, surrounded by wispy smoke and dark shadows, creating a surreal atmosphere.\",\n  \"Prompt21\": \"A female with blonde hair wearing a red satin style satin dress, leaving no mark as she fades in a dark bedroom, with a translucent and peaceful expression, surrounded by swirling mist and shadows, creating a vanishing atmosphere.\",\n  \"Prompt22\": \"A female with blonde hair wearing a red satin style satin dress, whispering a silent command in a dark bedroom, with a soft and final expression, surrounded by approaching shadows and moonlight, creating a quiet atmosphere.\",\n  \"Prompt23\": \"A female with blonde hair wearing a red satin style satin dress, fading away while staying the same in a dark bedroom, with a hollow and eternal expression, surrounded by a vanishing form and deep shadows, creating a melancholic atmosphere.\",\n  \"Prompt24\": \"A female with blonde hair wearing a red satin style satin dress, facing the end in a dark bedroom, with a calm and resigned expression, surrounded by encroaching shadows and a fogged mirror, creating a final atmosphere.\"\n}",
        100
      ],
      "color": "#2a363b",
      "bgcolor": "#3f5159",
      "shape": 1
    },
    {
      "id": 821,
      "type": "VRGDG_LoadTextAdvanced",
      "pos": [
        -60.226845849649436,
        6004.450614047111
      ],
      "size": [
        227,
        174
      ],
      "flags": {},
      "order": 66,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "text",
          "type": "STRING",
          "links": [
            1289
          ]
        },
        {
          "name": "file_path",
          "type": "STRING",
          "links": null
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_LoadTextAdvanced",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "subjectandscenes",
        true,
        "subjectsandscenes.txt",
        "",
        null
      ]
    },
    {
      "id": 812,
      "type": "VRGDG_ShowText",
      "pos": [
        532.8216444361606,
        6467.366886619301
      ],
      "size": [
        231.73392632670368,
        200.42667352689932
      ],
      "flags": {},
      "order": 111,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "shape": 7,
          "type": "STRING",
          "link": 1274
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowText",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "A female with blonde hair wearing a red satin style satin dress, facing the end in a dark bedroom, with a calm and resigned expression, surrounded by encroaching shadows and a fogged mirror, creating a final atmosphere."
      ]
    },
    {
      "id": 806,
      "type": "VRGDG_MultiStringConcat",
      "pos": [
        547.542796744941,
        6000.400832903359
      ],
      "size": [
        212.9,
        406
      ],
      "flags": {},
      "order": 110,
      "mode": 0,
      "inputs": [
        {
          "name": "string_2",
          "type": "STRING",
          "widget": {
            "name": "string_2"
          },
          "link": 1289
        },
        {
          "name": "string_4",
          "type": "STRING",
          "widget": {
            "name": "string_4"
          },
          "link": 1265
        },
        {
          "name": "string_6",
          "type": "STRING",
          "widget": {
            "name": "string_6"
          },
          "link": 1290
        }
      ],
      "outputs": [
        {
          "name": "text",
          "type": "STRING",
          "links": [
            1268,
            1291
          ]
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_MultiStringConcat",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        6,
        "\\n\\n",
        "\nSubject:",
        "Subject:\n",
        "\ncurrent visual prompt",
        "",
        "\nStyle/Theme:",
        "\n",
        "\nStory Idea:",
        "\n",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
      ]
    },
    {
      "id": 811,
      "type": "VRGDG_SuperGemmaGGUFChat",
      "pos": [
        246.30190806477867,
        5588.021709128911
      ],
      "size": [
        355.9556140957259,
        278
      ],
      "flags": {},
      "order": 143,
      "mode": 0,
      "inputs": [
        {
          "name": "custom_instructions",
          "type": "STRING",
          "widget": {
            "name": "custom_instructions"
          },
          "link": 1311
        },
        {
          "name": "user_input",
          "type": "STRING",
          "widget": {
            "name": "user_input"
          },
          "link": 1277
        }
      ],
      "outputs": [
        {
          "name": "text",
          "type": "STRING",
          "links": [
            1279,
            1285
          ]
        },
        {
          "name": "used_model",
          "type": "STRING",
          "links": []
        },
        {
          "name": "status",
          "type": "STRING",
          "links": []
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_SuperGemmaGGUFChat",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "supergemma4-26b-uncensored-fast-v2-Q4_K_M.gguf",
        "mmproj-BF16.gguf",
        "custom",
        "Convert the user’s text-to-image prompt into a dynamic image-to-video prompt.\n\nUse the image prompt only as the visual reference. Preserve the original subject, setting, outfit, mood, atmosphere, and scene identity. Do not repeat or describe color grading, lighting style, camera photo style, or static image-quality terms unless needed for motion clarity.\n\nAdd fast cinematic motion with natural pacing by giving the subject a clear action sequence, expressive body movement, strong gestures, and intentional camera movement. Keep the subject visible and framed throughout.\n\nOutput one polished paragraph using this structure (must be followed!!!!):\n\n[Subject] singing with passion in [setting/environment] during [time/weather]. The [subject], [fast cinematic action sequence with natural pacing, expressive body movement, strong gestures, and performance energy]. Their clothing/hair [reacts naturally to motion, wind, rain, or movement]. The camera [cinematic tracking, dolly, orbit, push-in, pull-back, handheld, crane, or smooth lateral movement] while maintaining [clear framing/visibility of the subject]. The environment [moves/reacts naturally: rain, fog, reflections, wind, dust, smoke, background motion, objects shifting, or atmosphere changing].\n\n[subject] = character gender - don't just say \"subject\"\n\nDo not add audio, dialogue, captions, text overlays, unrelated characters, new locations, major story changes, color style, lighting style, or image-quality descriptions. Keep it vivid, fast, cinematic, dynamic, and video-ready.\n\nReminder! The character MUST be singing with passion anytime they are mentioned!!!\n\nText-to-image prompt to convert:\n\n",
        "",
        "",
        0,
        false,
        true,
        7936,
        99,
        8,
        "",
        0.4,
        0.8,
        32000
      ],
      "color": "#322",
      "bgcolor": "#533"
    },
    {
      "id": 805,
      "type": "VRGDG_SuperGemmaGGUFChat",
      "pos": [
        786.1974713970465,
        5999.065519169586
      ],
      "size": [
        304.9,
        278
      ],
      "flags": {},
      "order": 124,
      "mode": 0,
      "inputs": [
        {
          "name": "user_input",
          "type": "STRING",
          "widget": {
            "name": "user_input"
          },
          "link": 1268
        }
      ],
      "outputs": [
        {
          "name": "text",
          "type": "STRING",
          "links": [
            1270,
            1277,
            1284
          ]
        },
        {
          "name": "used_model",
          "type": "STRING",
          "links": []
        },
        {
          "name": "status",
          "type": "STRING",
          "links": []
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_SuperGemmaGGUFChat",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        "supergemma4-26b-uncensored-fast-v2-Q4_K_M.gguf",
        "mmproj-BF16.gguf",
        "custom",
        "Create one text-to-image prompt from the user input.\n\nUser input includes:\n- subject\n- one current visual prompt\n- a style/theme\n\nUse all parts of the user input together.\n\nPriority:\n- Use the current visual prompt as the main scene foundation.\n- Keep the main action, subject, and setting from the current visual prompt unless the user clearly changes them.\n- Use the style/theme to control the visual aesthetic, color grading, lighting, mood, wardrobe refinement, environment design, and overall cinematic treatment.\n- Use the provided subject as the main subject of the image.\n\nRules:\n- Create one polished text-to-image prompt.\n- Treat the current visual prompt as the base scene description.\n- Expand and improve that scene using the style/theme.\n- Keep the image prompt concrete and visual.\n- Use the style/theme to influence color palette, tone, texture, lighting style, atmosphere, and production quality.\n- If the current visual prompt includes concrete objects, actions, reflections, or setting details, keep them visible in the final prompt.\n- Do not use metaphors, abstract symbolic wording, or non-visible language.\n- Do not use phrases like \"metaphorical thunder,\" \"invisible storm clouds,\" \"lightness of being,\" or other poetic abstractions.\n- Describe only things that can be seen in the final image.\n- Keep the result as one strong image prompt, not a summary.\n- Correct obvious typos, malformed words, and broken phrases from the current visual prompt before using it.\n- Fix spelling errors in character, clothing, objects, and setting details.\n- Preserve the intended meaning while cleaning the wording.\n- Do not mention that typos were fixed.\n- Do not explain your choices.\n- Only send the final prompt text.\n\nUse this exact format:\n\nA high resolution cinematic photograph of a [subject], [action or pose based primarily on the current visual prompt], in [environment/location shaped by the current visual prompt], during [time of day]. The subject is wearing [main outfit from the current visual prompt refined by the style/theme], [shoes/accessories from the current visual prompt refined by the style/theme], and [additional visible style details inspired by the style/theme]. Their hair is [hair color], [hair length/style], and [movement or texture]. The environment is [visual style of location from the current visual prompt shaped by the style/theme] with [background details that visibly represent the current visual prompt], [lighting and color grading details that match the style/theme], and [surface/reflection/material details connected to the current visual prompt and style/theme]. Camera is [camera angle] with a [lens type or framing]. The weather is [weather condition appropriate to the scene], with [atmospheric detail influenced by the style/theme], creating a [mood/style] mood.\n\n[subject] = character gender! don't just say \"subject\"!\n\nOnly send the final prompt text. Do not include labels, notes, quotes, or extra text.\n\nUser Input:\n",
        "",
        "",
        0,
        false,
        true,
        7936,
        99,
        8,
        "",
        0.4,
        0.8,
        32000
      ],
      "color": "#322",
      "bgcolor": "#533"
    },
    {
      "id": 829,
      "type": "VRGDG_ShowText",
      "pos": [
        206.47324414657263,
        6406.993470989022
      ],
      "size": [
        309.3460210035722,
        415.2624107006741
      ],
      "flags": {},
      "order": 125,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "shape": 7,
          "type": "STRING",
          "link": 1291
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowText",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": []
    },
    {
      "id": 273,
      "type": "VHS_VideoCombine",
      "pos": [
        2334.194163123061,
        5669.685261241699
      ],
      "size": [
        708.9428087060846,
        715.4361646432451
      ],
      "flags": {
        "collapsed": false
      },
      "order": 121,
      "mode": 0,
      "inputs": [
        {
          "name": "images",
          "type": "IMAGE",
          "link": 701
        },
        {
          "name": "audio",
          "shape": 7,
          "type": "AUDIO",
          "link": 699
        },
        {
          "name": "meta_batch",
          "shape": 7,
          "type": "VHS_BatchManager",
          "link": null
        },
        {
          "name": "vae",
          "shape": 7,
          "type": "VAE",
          "link": null
        },
        {
          "name": "frame_rate",
          "type": "FLOAT",
          "widget": {
            "name": "frame_rate"
          },
          "link": 1240
        },
        {
          "name": "filename_prefix",
          "type": "STRING",
          "widget": {
            "name": "filename_prefix"
          },
          "link": 697
        }
      ],
      "outputs": [
        {
          "name": "Filenames",
          "type": "VHS_FILENAMES",
          "links": [
            677
          ]
        }
      ],
      "properties": {
        "cnr_id": "comfyui-videohelpersuite",
        "ver": "1.7.9",
        "Node name for S&R": "VHS_VideoCombine",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": {
        "frame_rate": 25,
        "loop_count": 0,
        "filename_prefix": "AnimateDiff",
        "format": "video/h264-mp4",
        "pix_fmt": "yuv420p",
        "crf": 19,
        "save_metadata": true,
        "trim_to_audio": false,
        "pingpong": false,
        "save_output": true,
        "videopreview": {
          "hidden": false,
          "paused": true,
          "params": {
            "filename": "video_0024_0023_00001-audio.mp4",
            "subfolder": "Z:\\ComfyUI\\ComfyUI_windows_portable\\ComfyUI\\output\\Whisper in the Dark_2026-04-27_09-28-25",
            "type": "output",
            "format": "video/h264-mp4",
            "frame_rate": 24,
            "workflow": "video_0024_0023_00001.png",
            "fullpath": "Z:\\ComfyUI\\ComfyUI_windows_portable\\ComfyUI\\output\\Whisper in the Dark_2026-04-27_09-28-25\\video_0024_0023_00001-audio.mp4"
          }
        }
      },
      "color": "#323",
      "bgcolor": "#535",
      "shape": 1
    },
    {
      "id": 831,
      "type": "VRGDG_ShowText",
      "pos": [
        -219.7965679119036,
        5378.968710527508
      ],
      "size": [
        393.83310361304655,
        487.95716625717705
      ],
      "flags": {},
      "order": 106,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "shape": 7,
          "type": "STRING",
          "link": 1310
        }
      ],
      "outputs": [
        {
          "name": "text_output",
          "shape": 6,
          "type": "STRING",
          "links": null
        }
      ],
      "properties": {
        "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
        "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
        "Node name for S&R": "VRGDG_ShowText",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": []
    },
    {
      "id": 828,
      "type": "MarkdownNote",
      "pos": [
        -368.6988535855963,
        4964.415974910521
      ],
      "size": [
        262.8459735736701,
        263.924316132292
      ],
      "flags": {},
      "order": 67,
      "mode": 0,
      "inputs": [],
      "outputs": [],
      "title": "WALK THROUGH VIDOE",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "# Full Workflow Walkthrough Video\n\nThis video walks through the complete Nano Banana process  \nfrom start to finish using a real video project.\n\n### 🎬 Walkthrough Video\n🔗 [Watch the Video](https://youtu.be/pxwk1rNdNh4)\n\nShows full setup, prompt workflow, reference image usage,\nand the exact process used to produce the final result."
      ],
      "color": "#232",
      "bgcolor": "#353"
    },
    {
      "id": 483,
      "type": "MarkdownNote",
      "pos": [
        0.025053182150033493,
        5155.203157770696
      ],
      "size": [
        210,
        112.58147512751657
      ],
      "flags": {},
      "order": 68,
      "mode": 0,
      "inputs": [],
      "outputs": [],
      "title": "Settings",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "# ➡️➡️➡️ UPDATE YOUR SETTINGS ➡️➡️➡️\n"
      ],
      "color": "#232",
      "bgcolor": "#353",
      "shape": 1
    },
    {
      "id": 830,
      "type": "dd449f08-b59d-45b5-b1de-1a23ab740fc1",
      "pos": [
        -572.3795131667514,
        5376.936143004834
      ],
      "size": [
        334.856330565437,
        479.21860970977104
      ],
      "flags": {
        "collapsed": false
      },
      "order": 69,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {
          "name": "text",
          "type": "STRING",
          "links": [
            1310,
            1311
          ]
        }
      ],
      "properties": {
        "proxyWidgets": [
          [
            "-1",
            "index"
          ],
          [
            "-1",
            "string_1"
          ],
          [
            "-1",
            "items"
          ],
          [
            "-1",
            "label"
          ],
          [
            "-1",
            "pick_count"
          ],
          [
            "-1",
            "selection_mode"
          ],
          [
            "-1",
            "two_item_template"
          ]
        ],
        "cnr_id": "comfy-core",
        "ver": "0.16.2",
        "ue_properties": {
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {},
          "version": "7.5.2"
        }
      },
      "widgets_values": [
        0,
        "Convert the user’s text-to-image prompt into a dynamic image-to-video prompt.\n\nUse the image prompt only as the visual reference. Preserve the original subject, setting, outfit, mood, atmosphere, and scene identity. Do not repeat or describe color grading, lighting style, camera photo style, or static image-quality terms unless needed for motion clarity.\n\nAdd fast, cinematic motion by giving the subject a clear action sequence, expressive face expressions and body movement, strong gestures, and intentional camera movement. Keep the subject visible and framed throughout.\n\nOutput one polished paragraph using this structure:\n\nThe [Subject] who is singing with passion in [setting/environment] during [time/weather]. The subject [dynamic performance action]. Their clothing/hair [reacts to movement]. The camera [Camera Motion] while maintaining [subject visibility]. The environment [reacts dynamically].\n\neach word in brackets should be chosen based of user input that would best fit the scene.\nNOTE: DO NOT USE ORBIT TYPE CAMERA MOTION, DO NOT USE THE WORD \"SPIN\" SUBJECT SHOULD NEVER SPIN \nSubject should always be physically singing!\n\nDo not add audio, dialogue, captions, text overlays, unrelated characters, new locations, major story changes, color style, lighting style, or image-quality descriptions. Keep it vivid, fast, cinematic, dynamic, and video-ready.\n",
        "slow push in\nslow pull out\ndolly in\ndolly out\ntruck left\ntruck right\npan left\npan right\ntilt up\ntilt down\ncrane up\ncrane down\norbit left\norbit right\nhandheld follow\nwhip pan\nrack focus\nlow angle tracking shot\noverhead descending shot\nsteadicam walk forward\n",
        "Camera Motion",
        2,
        "index",
        "begin with {item1}, then transition into {item2}"
      ]
    },
    {
      "id": 832,
      "type": "MarkdownNote",
      "pos": [
        1640.6248250986725,
        5069.566845671092
      ],
      "size": [
        332.8944328777659,
        184.5699087446501
      ],
      "flags": {},
      "order": 70,
      "mode": 0,
      "inputs": [],
      "outputs": [],
      "title": "LLM MODEL",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "# Model Download\n\nDownload the model here:\n\n[supergemma4-26b-uncensored-fast-v2-Q4_K_M.gguf](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2/resolve/main/supergemma4-26b-uncensored-fast-v2-Q4_K_M.gguf)\n\n[mmproj-BF16.gguf](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF/resolve/main/mmproj-BF16.gguf)\n\nPlace both downloaded files here:\n\n```text\nModels/LLM"
      ],
      "color": "#222",
      "bgcolor": "#000"
    },
    {
      "id": 796,
      "type": "MarkdownNote",
      "pos": [
        1006.415452712399,
        4496.46427912615
      ],
      "size": [
        612.0800601540543,
        763.8606020190255
      ],
      "flags": {},
      "order": 71,
      "mode": 0,
      "inputs": [],
      "outputs": [],
      "title": "LTX models used in  this workflow",
      "properties": {
        "ue_properties": {
          "widget_ue_connectable": {},
          "version": "7.5.2",
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "## 📦 Required Models & Assets\n\n### 🧠 Diffusion Model\n- **ltx-2.3-distilled gguf models**  \n  🔗 [Download](https://huggingface.co/Abiray/LTX-2.3-22B-DISTILLED-1.1-GGUF/tree/main)\n\n---\n\n### 🎥 Video & 🔊 Audio VAE\n- **LTX2.3_video_vae_bf16.safetensors**  \n- **LTX2.3_audio_vae_bf16.safetensors**  \n  🔗 [Download](https://huggingface.co/Kijai/LTX2.3_comfy/tree/main/vae)\n\n---\n\n### 📝Clip Text / Instruction Model\n- **gemma-3-12b-it-abliterated-sikaworld-high-fidelity-edition.safetensors**  \n  🔗 [Download](https://huggingface.co/Sikaworld1990/gemma-3-12b-it-abliterated-sikaworld-high-fidelity-edition-Ltx-2/resolve/main/gemma-3-12b-it-abliterated-sikaworld-high-fidelity-edition.safetensors)\n\n---\n\n### 🔤 Clip Text Encoder / Embeddings\n- **ltx-2.3_text_projection_bf16.safetensors**  \n  🔗 [Download](https://huggingface.co/Kijai/LTX2.3_comfy/tree/main/text_encoders)\n\n---\n\n### 🔍 Spatial Upscaler\n- **ltx-2.3-spatial-upscaler-x2-1.1.safetensors**  \n  🔗 [Download](https://huggingface.co/prince-canuma/LTX-2.3-distilled/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors)\n\n---\n\n```\n📂 ComfyUI/\n├── 📂 models/\n│   ├── 📂 diffusion_models/\n│   │      └── ltx-2.3-distilled_1.1-Q6_k.gguf\n│   ├── 📂 text_encoders/\n│   │      ├── ltx-2.3-text_projection_bf16.safetensors\n│   │      └── gemma Model\n│   ├── 📂 vae/\n│   │      ├── LTX2.3_video_vae_bf16.safetensors\n│   │      └── LTX2.3_audio_vae_bf16.safetensors\n│   └── 📂 latent_upscale_models/\n│          └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors\n\n```\n"
      ],
      "color": "#432",
      "bgcolor": "#653",
      "shape": 1
    },
    {
      "id": 797,
      "type": "3cae606b-5e3e-4046-8c9f-8fffd361c513",
      "pos": [
        1103.3029086940076,
        5998.413751309942
      ],
      "size": [
        462.7062195060796,
        334
      ],
      "flags": {},
      "order": 144,
      "mode": 0,
      "inputs": [
        {
          "name": "text",
          "type": "STRING",
          "widget": {
            "name": "text"
          },
          "link": 1284
        }
      ],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [
            1249
          ]
        }
      ],
      "properties": {
        "proxyWidgets": [
          [
            "-1",
            "text"
          ],
          [
            "-1",
            "text_1"
          ],
          [
            "-1",
            "seed"
          ],
          [
            "-1",
            "width"
          ],
          [
            "-1",
            "height"
          ],
          [
            "-1",
            "lora_name"
          ],
          [
            "-1",
            "strength_model"
          ],
          [
            "-1",
            "unet_name"
          ],
          [
            "-1",
            "clip_name"
          ],
          [
            "-1",
            "vae_name"
          ]
        ],
        "cnr_id": "comfy-core",
        "ver": "0.3.75",
        "ue_properties": {
          "version": "7.5.2",
          "widget_ue_connectable": {},
          "input_ue_unconnectable": {}
        }
      },
      "widgets_values": [
        "A cinematic HDR headshot photograph of a female fashion model with smooth olive skin, long wavy dark brown hair flowing over her shoulders, and striking green eyes. She wears a sleek black blazer and subtle gold earrings. The mood is elegant and confident. The background is a softly blurred upscale studio with neutral matte tones that enhance her features. Camera angle is eye-level and tightly framed on her face with shallow depth of field. Soft studio lighting highlights her cheekbones. The scene is indoors during the daytime with controlled studio lighting, ultra-sharp focus, professional fashion photography style.",
        "bad hands, extra fingers, missing fingers, fused fingers, broken hands, mutant hands, twisted limbs, extra limbs, missing limbs, dimple ",
        500,
        1280,
        720,
        "BlondeFemaleCharacterLora.safetensors",
        0.8,
        "z_image_turbo_bf16.safetensors",
        "qwen_3_4b.safetensors",
        "ae.safetensors"
      ],
      "color": "#323",
      "bgcolor": "#535"
    }
  ],
  "links": [
    [
      635,
      271,
      0,
      339,
      0,
      "VAE"
    ],
    [
      636,
      271,
      1,
      340,
      0,
      "CLIP"
    ],
    [
      637,
      271,
      2,
      341,
      0,
      "LATENT_UPSCALE_MODEL"
    ],
    [
      638,
      271,
      3,
      342,
      0,
      "VAE"
    ],
    [
      639,
      271,
      4,
      343,
      0,
      "MODEL"
    ],
    [
      640,
      346,
      0,
      218,
      4,
      "VAE"
    ],
    [
      641,
      347,
      0,
      218,
      3,
      "VAE"
    ],
    [
      642,
      348,
      0,
      231,
      0,
      "CLIP"
    ],
    [
      643,
      349,
      0,
      218,
      0,
      "MODEL"
    ],
    [
      644,
      350,
      0,
      219,
      3,
      "LATENT_UPSCALE_MODEL"
    ],
    [
      645,
      351,
      0,
      219,
      4,
      "VAE"
    ],
    [
      646,
      352,
      0,
      219,
      0,
      "MODEL"
    ],
    [
      647,
      219,
      0,
      355,
      0,
      "LATENT"
    ],
    [
      648,
      356,
      0,
      268,
      0,
      "LATENT"
    ],
    [
      649,
      357,
      0,
      236,
      0,
      "LATENT"
    ],
    [
      650,
      218,
      0,
      358,
      0,
      "LATENT"
    ],
    [
      651,
      359,
      0,
      219,
      7,
      "LATENT"
    ],
    [
      652,
      360,
      0,
      269,
      0,
      "*"
    ],
    [
      653,
      362,
      0,
      236,
      1,
      "VAE"
    ],
    [
      654,
      361,
      0,
      236,
      2,
      "VAE"
    ],
    [
      662,
      218,
      2,
      369,
      0,
      "INT"
    ],
    [
      666,
      218,
      3,
      370,
      0,
      "STRING"
    ],
    [
      667,
      384,
      0,
      297,
      1,
      "STRING"
    ],
    [
      668,
      385,
      0,
      297,
      2,
      "STRING"
    ],
    [
      669,
      218,
      4,
      372,
      0,
      "STRING"
    ],
    [
      671,
      218,
      5,
      373,
      0,
      "STRING"
    ],
    [
      674,
      218,
      6,
      371,
      0,
      "INT"
    ],
    [
      675,
      218,
      8,
      375,
      0,
      "STRING"
    ],
    [
      677,
      273,
      0,
      388,
      0,
      "VHS_FILENAMES"
    ],
    [
      679,
      231,
      0,
      390,
      0,
      "CONDITIONING"
    ],
    [
      680,
      391,
      0,
      233,
      0,
      "CONDITIONING"
    ],
    [
      681,
      233,
      0,
      392,
      0,
      "CONDITIONING"
    ],
    [
      682,
      393,
      0,
      181,
      0,
      "CONDITIONING"
    ],
    [
      683,
      394,
      0,
      181,
      1,
      "CONDITIONING"
    ],
    [
      684,
      181,
      0,
      395,
      0,
      "CONDITIONING"
    ],
    [
      685,
      181,
      1,
      396,
      0,
      "CONDITIONING"
    ],
    [
      686,
      397,
      0,
      219,
      1,
      "CONDITIONING"
    ],
    [
      687,
      398,
      0,
      219,
      2,
      "CONDITIONING"
    ],
    [
      690,
      402,
      0,
      218,
      1,
      "CONDITIONING"
    ],
    [
      691,
      403,
      0,
      218,
      2,
      "CONDITIONING"
    ],
    [
      693,
      218,
      9,
      376,
      0,
      "STRING"
    ],
    [
      697,
      407,
      0,
      273,
      5,
      "STRING"
    ],
    [
      699,
      409,
      0,
      273,
      1,
      "AUDIO"
    ],
    [
      701,
      411,
      0,
      273,
      0,
      "IMAGE"
    ],
    [
      702,
      218,
      7,
      374,
      0,
      "INT"
    ],
    [
      703,
      218,
      10,
      377,
      0,
      "AUDIO"
    ],
    [
      704,
      218,
      11,
      378,
      0,
      "INT"
    ],
    [
      705,
      218,
      12,
      379,
      0,
      "INT"
    ],
    [
      706,
      235,
      0,
      412,
      0,
      "NOISE"
    ],
    [
      707,
      413,
      0,
      218,
      8,
      "NOISE"
    ],
    [
      711,
      218,
      10,
      417,
      0,
      "AUDIO"
    ],
    [
      712,
      418,
      0,
      311,
      0,
      "AUDIO"
    ],
    [
      714,
      420,
      0,
      297,
      0,
      "AUDIO"
    ],
    [
      716,
      236,
      1,
      422,
      0,
      "IMAGE"
    ],
    [
      723,
      434,
      0,
      218,
      10,
      "INT"
    ],
    [
      724,
      435,
      0,
      218,
      5,
      "INT"
    ],
    [
      725,
      436,
      0,
      218,
      6,
      "INT"
    ],
    [
      726,
      437,
      0,
      438,
      0,
      "STRING"
    ],
    [
      727,
      439,
      0,
      218,
      9,
      "STRING"
    ],
    [
      731,
      444,
      0,
      181,
      2,
      "FLOAT"
    ],
    [
      735,
      451,
      0,
      235,
      0,
      "INT"
    ],
    [
      737,
      455,
      0,
      218,
      11,
      "AUDIO"
    ],
    [
      797,
      414,
      0,
      530,
      1,
      "INT"
    ],
    [
      798,
      423,
      0,
      530,
      0,
      "IMAGE"
    ],
    [
      799,
      530,
      0,
      410,
      0,
      "IMAGE"
    ],
    [
      814,
      540,
      0,
      530,
      4,
      "INT"
    ],
    [
      845,
      553,
      0,
      218,
      14,
      "INT"
    ],
    [
      897,
      586,
      0,
      543,
      0,
      "INT"
    ],
    [
      900,
      588,
      0,
      231,
      1,
      "STRING"
    ],
    [
      912,
      297,
      0,
      408,
      0,
      "AUDIO"
    ],
    [
      916,
      218,
      12,
      604,
      0,
      "INT"
    ],
    [
      917,
      605,
      0,
      530,
      2,
      "INT"
    ],
    [
      918,
      606,
      0,
      530,
      3,
      "INT"
    ],
    [
      950,
      631,
      0,
      218,
      7,
      "IMAGE"
    ],
    [
      951,
      631,
      0,
      219,
      5,
      "IMAGE"
    ],
    [
      953,
      404,
      0,
      634,
      0,
      "STRING"
    ],
    [
      954,
      382,
      0,
      634,
      1,
      "INT"
    ],
    [
      955,
      405,
      0,
      634,
      2,
      "STRING"
    ],
    [
      956,
      634,
      0,
      406,
      0,
      "STRING"
    ],
    [
      957,
      218,
      8,
      635,
      0,
      "STRING"
    ],
    [
      958,
      635,
      0,
      632,
      1,
      "STRING"
    ],
    [
      970,
      389,
      0,
      640,
      0,
      "VHS_FILENAMES"
    ],
    [
      971,
      463,
      0,
      640,
      1,
      "AUDIO"
    ],
    [
      972,
      386,
      0,
      640,
      2,
      "INT"
    ],
    [
      973,
      387,
      0,
      640,
      3,
      "STRING"
    ],
    [
      1074,
      686,
      0,
      218,
      13,
      "STRING"
    ],
    [
      1079,
      690,
      0,
      686,
      0,
      "INT"
    ],
    [
      1080,
      690,
      0,
      686,
      1,
      "INT"
    ],
    [
      1150,
      736,
      0,
      429,
      0,
      "INT"
    ],
    [
      1151,
      736,
      1,
      430,
      0,
      "INT"
    ],
    [
      1152,
      736,
      2,
      450,
      0,
      "INT"
    ],
    [
      1154,
      736,
      4,
      454,
      0,
      "AUDIO"
    ],
    [
      1155,
      736,
      5,
      431,
      0,
      "INT"
    ],
    [
      1157,
      736,
      6,
      737,
      0,
      "STRING"
    ],
    [
      1158,
      736,
      7,
      738,
      0,
      "STRING"
    ],
    [
      1185,
      736,
      3,
      437,
      0,
      "STRING"
    ],
    [
      1188,
      686,
      0,
      755,
      0,
      "STRING"
    ],
    [
      1192,
      445,
      0,
      760,
      0,
      "INT"
    ],
    [
      1193,
      761,
      0,
      758,
      0,
      "INT"
    ],
    [
      1194,
      383,
      0,
      762,
      0,
      "STRING"
    ],
    [
      1205,
      770,
      0,
      632,
      0,
      "IMAGE"
    ],
    [
      1206,
      768,
      0,
      630,
      0,
      "IMAGE"
    ],
    [
      1234,
      736,
      8,
      552,
      0,
      "INT"
    ],
    [
      1237,
      736,
      5,
      794,
      0,
      "INT"
    ],
    [
      1238,
      794,
      0,
      443,
      0,
      "FLOAT"
    ],
    [
      1239,
      537,
      0,
      795,
      0,
      "INT"
    ],
    [
      1240,
      795,
      0,
      273,
      4,
      "FLOAT"
    ],
    [
      1249,
      797,
      0,
      768,
      0,
      "IMAGE"
    ],
    [
      1265,
      543,
      0,
      806,
      1,
      "STRING"
    ],
    [
      1268,
      806,
      0,
      805,
      0,
      "STRING"
    ],
    [
      1270,
      805,
      0,
      810,
      0,
      "STRING"
    ],
    [
      1274,
      543,
      0,
      812,
      0,
      "STRING"
    ],
    [
      1277,
      805,
      0,
      811,
      1,
      "STRING"
    ],
    [
      1279,
      811,
      0,
      815,
      0,
      "STRING"
    ],
    [
      1284,
      805,
      0,
      797,
      0,
      "STRING"
    ],
    [
      1285,
      811,
      0,
      587,
      0,
      "STRING"
    ],
    [
      1289,
      821,
      0,
      806,
      0,
      "STRING"
    ],
    [
      1290,
      817,
      0,
      806,
      2,
      "STRING"
    ],
    [
      1291,
      806,
      0,
      829,
      0,
      "STRING"
    ],
    [
      1310,
      830,
      0,
      831,
      0,
      "STRING"
    ],
    [
      1311,
      830,
      0,
      811,
      0,
      "STRING"
    ]
  ],
  "groups": [
    {
      "id": 6,
      "title": "LTX Models",
      "bounding": [
        229.61927450575774,
        4658.269656104114,
        745.9087007029761,
        398.8292030198363
      ],
      "color": "#3f789e",
      "font_size": 24,
      "flags": {}
    },
    {
      "id": 7,
      "title": "LTX",
      "bounding": [
        227.54210806681556,
        5505.495871571411,
        1373.051184616351,
        391.9557801854653
      ],
      "color": "#3f789e",
      "font_size": 24,
      "flags": {}
    },
    {
      "id": 8,
      "title": "Settings",
      "bounding": [
        226.99049170324434,
        5075.7404106522,
        704.2704778051939,
        414.02485346437516
      ],
      "color": "#3f789e",
      "font_size": 24,
      "flags": {}
    },
    {
      "id": 9,
      "title": "LTX",
      "bounding": [
        1614.5219331873263,
        5506.122357835495,
        674.9103997088278,
        897.2642362404176
      ],
      "color": "#3f789e",
      "font_size": 24,
      "flags": {}
    },
    {
      "id": 12,
      "title": "video chunk",
      "bounding": [
        2306.6659368823816,
        5510.564235634293,
        748.2026315656803,
        1187.2069779857347
      ],
      "color": "#3f789e",
      "font_size": 24,
      "flags": {}
    },
    {
      "id": 18,
      "title": "Outputs for display",
      "bounding": [
        949.4597186436595,
        5297.257744592233,
        448.6380009617867,
        189.99707143210526
      ],
      "color": "#3f789e",
      "font_size": 24,
      "flags": {}
    },
    {
      "id": 21,
      "title": "image",
      "bounding": [
        1631.4711942330491,
        6415.560099627953,
        650.6486793045156,
        504.0738213257109
      ],
      "color": "#3f789e",
      "font_size": 24,
      "flags": {}
    },
    {
      "id": 24,
      "title": "zimage",
      "bounding": [
        -80.20066265034941,
        5912.274483665841,
        1673.3157404546448,
        933.6000832741775
      ],
      "color": "#3f789e",
      "font_size": 24,
      "flags": {}
    },
    {
      "id": 27,
      "title": "Group",
      "bounding": [
        -582.3795131667514,
        5303.3361430048335,
        790.4617785562996,
        590.1211729406295
      ],
      "color": "#3f789e",
      "font_size": 24,
      "flags": {}
    }
  ],
  "definitions": {
    "subgraphs": [
      {
        "id": "5548df69-fe42-439c-993d-20f06190baa7",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "LTX2",
        "inputNode": {
          "id": -10,
          "bounding": [
            -679.5856091781292,
            7034.57833497376,
            161,
            460
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            269.77112479688833,
            7101.3501631460695,
            143,
            300
          ]
        },
        "inputs": [
          {
            "id": "4b2afb33-fb3f-4f9a-b7e2-b4118b52a632",
            "name": "model",
            "type": "MODEL",
            "linkIds": [
              378
            ],
            "localized_name": "model",
            "pos": [
              -538.5856091781292,
              7054.57833497376
            ]
          },
          {
            "id": "347b6d03-00e3-4e4b-a478-4a2c4c1b3b07",
            "name": "positive",
            "type": "CONDITIONING",
            "linkIds": [
              379
            ],
            "localized_name": "positive",
            "pos": [
              -538.5856091781292,
              7074.57833497376
            ]
          },
          {
            "id": "ca10f0ca-107e-4d8f-b2f9-d78d01f1111c",
            "name": "negative",
            "type": "CONDITIONING",
            "linkIds": [
              380
            ],
            "localized_name": "negative",
            "pos": [
              -538.5856091781292,
              7094.57833497376
            ]
          },
          {
            "id": "18424927-cab9-4266-ba01-dc52caab6546",
            "name": "vae",
            "type": "VAE",
            "linkIds": [
              428
            ],
            "pos": [
              -538.5856091781292,
              7114.57833497376
            ]
          },
          {
            "id": "2a45a1ee-8d85-4ef9-9054-e4a001cc5cc5",
            "name": "audio_vae",
            "type": "VAE",
            "linkIds": [
              429,
              471
            ],
            "pos": [
              -538.5856091781292,
              7134.57833497376
            ]
          },
          {
            "id": "e079d61f-fae6-4e32-bed6-7a17964cbc0a",
            "name": "width",
            "type": "INT",
            "linkIds": [
              469,
              580
            ],
            "pos": [
              -538.5856091781292,
              7154.57833497376
            ]
          },
          {
            "id": "f1038fbe-b900-4950-9d06-acc78d12223b",
            "name": "height",
            "type": "INT",
            "linkIds": [
              470,
              581
            ],
            "pos": [
              -538.5856091781292,
              7174.57833497376
            ]
          },
          {
            "id": "27515c85-62a7-44d8-ac4f-010b31620d0a",
            "name": "image",
            "type": "IMAGE",
            "linkIds": [
              579,
              584
            ],
            "pos": [
              -538.5856091781292,
              7194.57833497376
            ]
          },
          {
            "id": "ded41a7f-dc5a-49d9-907f-aa0e803709f9",
            "name": "noise",
            "type": "NOISE",
            "linkIds": [
              437
            ],
            "pos": [
              -538.5856091781292,
              7214.57833497376
            ]
          },
          {
            "id": "28d15068-842d-4ab7-8631-f58922209ae9",
            "name": "folder_path",
            "type": "STRING",
            "linkIds": [
              611
            ],
            "pos": [
              -538.5856091781292,
              7234.57833497376
            ]
          },
          {
            "id": "2a5d5f98-6085-4bec-bdf8-2712667a1bcc",
            "name": "fps",
            "type": "INT",
            "linkIds": [
              607,
              608
            ],
            "pos": [
              -538.5856091781292,
              7254.57833497376
            ]
          },
          {
            "id": "f9333b3a-9303-43a3-aa98-c2f86a2be6c9",
            "name": "audio",
            "type": "AUDIO",
            "linkIds": [
              609
            ],
            "pos": [
              -538.5856091781292,
              7274.57833497376
            ]
          },
          {
            "id": "915efb09-e5ab-4393-b4cd-e8987d33168d",
            "name": "model_name",
            "type": "COMBO",
            "linkIds": [],
            "label": "Mel-band Former",
            "pos": [
              -538.5856091781292,
              7294.57833497376
            ]
          },
          {
            "id": "ab8668aa-f165-495c-9d85-f8468eba29ce",
            "name": "srt_file",
            "type": "STRING",
            "linkIds": [
              627
            ],
            "pos": [
              -538.5856091781292,
              7314.57833497376
            ]
          },
          {
            "id": "cc2c9dc5-7b41-4d35-a106-a3b6a4eaf469",
            "name": "enable_auto_queue_1",
            "type": "BOOLEAN",
            "linkIds": [
              629
            ],
            "pos": [
              -538.5856091781292,
              7334.57833497376
            ]
          },
          {
            "id": "d6ef3e21-d073-4afc-af5a-69afeb33730b",
            "name": "redo_prompt_number",
            "type": "INT",
            "linkIds": [
              630
            ],
            "pos": [
              -538.5856091781292,
              7354.57833497376
            ]
          },
          {
            "id": "61a38e53-fec9-4bfb-847a-9d79881dd49a",
            "name": "overwrite_mode",
            "type": "COMBO",
            "linkIds": [
              631
            ],
            "pos": [
              -538.5856091781292,
              7374.57833497376
            ]
          },
          {
            "id": "00bcbdf4-b61f-42ae-8ff1-6e4df03b7c9f",
            "name": "tail_loss_frames",
            "type": "INT",
            "linkIds": [
              632
            ],
            "pos": [
              -538.5856091781292,
              7394.57833497376
            ]
          },
          {
            "id": "d406ad9e-7558-4134-98b9-6923787d6efa",
            "name": "pre_frames",
            "type": "INT",
            "linkIds": [
              633
            ],
            "pos": [
              -538.5856091781292,
              7414.57833497376
            ]
          },
          {
            "id": "4d11f9bd-d8e3-4d11-9712-1308570fefac",
            "name": "fixed_duration",
            "type": "INT",
            "linkIds": [
              634
            ],
            "pos": [
              -538.5856091781292,
              7434.57833497376
            ]
          },
          {
            "id": "32cf9021-54f9-40ca-938f-108f5ad3d3cc",
            "name": "use_remake_folder",
            "type": "BOOLEAN",
            "linkIds": [
              635
            ],
            "pos": [
              -538.5856091781292,
              7454.57833497376
            ]
          }
        ],
        "outputs": [
          {
            "id": "60fdc632-b47f-4fb1-803a-59ce11fab137",
            "name": "denoised_output",
            "type": "LATENT",
            "linkIds": [
              423
            ],
            "pos": [
              289.77112479688833,
              7121.3501631460695
            ]
          },
          {
            "id": "72e2a188-f038-4937-8dac-2851a4806e9f",
            "name": "total_duration",
            "type": "FLOAT",
            "linkIds": [
              612
            ],
            "pos": [
              289.77112479688833,
              7141.3501631460695
            ]
          },
          {
            "id": "852a34e8-268c-4e36-a1eb-2f00143a8b48",
            "name": "index",
            "type": "INT",
            "linkIds": [
              613
            ],
            "pos": [
              289.77112479688833,
              7161.3501631460695
            ]
          },
          {
            "id": "c7b4175c-7159-45a8-86ef-d6d019e7be23",
            "name": "start_time",
            "type": "STRING",
            "linkIds": [
              615
            ],
            "pos": [
              289.77112479688833,
              7181.3501631460695
            ]
          },
          {
            "id": "98b24b9f-f535-46c2-befd-055ba0d61f6b",
            "name": "end_time",
            "type": "STRING",
            "linkIds": [
              616
            ],
            "pos": [
              289.77112479688833,
              7201.3501631460695
            ]
          },
          {
            "id": "fd1120af-f83a-4f6d-aca1-94d17bf28b9e",
            "name": "instructions",
            "type": "STRING",
            "linkIds": [
              617
            ],
            "pos": [
              289.77112479688833,
              7221.3501631460695
            ]
          },
          {
            "id": "7e4a58ce-f283-4afc-9308-e84ab04db289",
            "name": "total_sets",
            "type": "INT",
            "linkIds": [
              618
            ],
            "pos": [
              289.77112479688833,
              7241.3501631460695
            ]
          },
          {
            "id": "dfb9c01c-5d26-44d7-b670-0c71528f796c",
            "name": "frames_per_scene",
            "type": "INT",
            "linkIds": [
              619
            ],
            "pos": [
              289.77112479688833,
              7261.3501631460695
            ]
          },
          {
            "id": "1478852d-1e8a-40f9-ad15-bfdcc34b78c3",
            "name": "output_folder",
            "type": "STRING",
            "linkIds": [
              622
            ],
            "pos": [
              289.77112479688833,
              7281.3501631460695
            ]
          },
          {
            "id": "c37d2e0b-ab1c-490b-8e3e-2b7704593afb",
            "name": "overwrite_mode",
            "type": "STRING",
            "linkIds": [
              623
            ],
            "pos": [
              289.77112479688833,
              7301.3501631460695
            ]
          },
          {
            "id": "70232f17-2948-4b4a-aa14-49ff6af842d7",
            "name": "audio_1",
            "type": "AUDIO",
            "linkIds": [
              624
            ],
            "pos": [
              289.77112479688833,
              7321.3501631460695
            ]
          },
          {
            "id": "7caf5a0e-bacf-458c-8f9b-c73aa8688ebe",
            "name": "frames_for_ltx",
            "type": "INT",
            "linkIds": [
              614
            ],
            "pos": [
              289.77112479688833,
              7341.3501631460695
            ]
          },
          {
            "id": "91763bea-969f-4a1b-b9d9-00176830d941",
            "name": "preroll_frames",
            "type": "INT",
            "linkIds": [
              621
            ],
            "pos": [
              289.77112479688833,
              7361.3501631460695
            ]
          }
        ],
        "widgets": [],
        "nodes": [
          {
            "id": 186,
            "type": "KSamplerSelect",
            "pos": [
              924.4998485292136,
              6936.928217971786
            ],
            "size": [
              270,
              73.99739583333334
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "SAMPLER",
                "name": "SAMPLER",
                "type": "SAMPLER",
                "links": [
                  385
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.71",
              "Node name for S&R": "KSamplerSelect",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "euler"
            ]
          },
          {
            "id": 199,
            "type": "LTXVConcatAVLatent",
            "pos": [
              932.248771819661,
              7239.246840225007
            ],
            "size": [
              270,
              60
            ],
            "flags": {
              "collapsed": false
            },
            "order": 6,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "video_latent",
                "name": "video_latent",
                "type": "LATENT",
                "link": 426
              },
              {
                "localized_name": "audio_latent",
                "name": "audio_latent",
                "type": "LATENT",
                "link": 468
              }
            ],
            "outputs": [
              {
                "localized_name": "latent",
                "name": "latent",
                "type": "LATENT",
                "links": [
                  387
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.5.1",
              "Node name for S&R": "LTXVConcatAVLatent",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 280,
            "type": "LTXVPreprocess",
            "pos": [
              545.7340196318952,
              7128.196640327747
            ],
            "size": [
              210,
              58
            ],
            "flags": {},
            "order": 18,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "image",
                "name": "image",
                "type": "IMAGE",
                "link": 584
              }
            ],
            "outputs": [
              {
                "localized_name": "output_image",
                "name": "output_image",
                "type": "IMAGE",
                "links": [
                  585
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.8.2",
              "Node name for S&R": "LTXVPreprocess",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              33
            ]
          },
          {
            "id": 200,
            "type": "PrimitiveInt",
            "pos": [
              597.4633612309127,
              6799.994204336662
            ],
            "size": [
              210,
              82
            ],
            "flags": {},
            "order": 7,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "value",
                "name": "value",
                "type": "INT",
                "widget": {
                  "name": "value"
                },
                "link": 626
              }
            ],
            "outputs": [
              {
                "localized_name": "INT",
                "name": "INT",
                "type": "INT",
                "links": [
                  371,
                  375
                ]
              }
            ],
            "title": "Frame Count",
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.5.1",
              "Node name for S&R": "PrimitiveInt",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              120,
              "fixed"
            ]
          },
          {
            "id": 185,
            "type": "CFGGuider",
            "pos": [
              952.4135843589895,
              6753.477010342601
            ],
            "size": [
              267.66455080775677,
              98
            ],
            "flags": {
              "collapsed": false
            },
            "order": 5,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "model",
                "name": "model",
                "type": "MODEL",
                "link": 378
              },
              {
                "localized_name": "positive",
                "name": "positive",
                "type": "CONDITIONING",
                "link": 379
              },
              {
                "localized_name": "negative",
                "name": "negative",
                "type": "CONDITIONING",
                "link": 380
              }
            ],
            "outputs": [
              {
                "localized_name": "GUIDER",
                "name": "GUIDER",
                "type": "GUIDER",
                "links": [
                  384
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.71",
              "Node name for S&R": "CFGGuider",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              1
            ]
          },
          {
            "id": 279,
            "type": "ResizeImageMaskNode",
            "pos": [
              313.05018475947554,
              6468.713426352148
            ],
            "size": [
              284.375,
              154
            ],
            "flags": {},
            "order": 17,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "input",
                "name": "input",
                "type": "IMAGE,MASK",
                "link": 579
              },
              {
                "localized_name": "width",
                "name": "resize_type.width",
                "type": "INT",
                "widget": {
                  "name": "resize_type.width"
                },
                "link": 580
              },
              {
                "localized_name": "height",
                "name": "resize_type.height",
                "type": "INT",
                "widget": {
                  "name": "resize_type.height"
                },
                "link": 581
              }
            ],
            "outputs": [
              {
                "localized_name": "resized",
                "name": "resized",
                "type": "IMAGE",
                "links": [
                  576
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.7.0",
              "Node name for S&R": "ResizeImageMaskNode",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              },
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65
            },
            "widgets_values": [
              "scale dimensions",
              736,
              416,
              "center",
              "lanczos"
            ]
          },
          {
            "id": 277,
            "type": "ImageScaleBy",
            "pos": [
              672.4210114260138,
              6536.1739220115505
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 15,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "image",
                "name": "image",
                "type": "IMAGE",
                "link": 577
              }
            ],
            "outputs": [
              {
                "localized_name": "IMAGE",
                "name": "IMAGE",
                "type": "IMAGE",
                "links": [
                  578
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "ImageScaleBy",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              "lanczos",
              0.5
            ]
          },
          {
            "id": 276,
            "type": "GetImageSize",
            "pos": [
              450.9569393084654,
              6274.446659361016
            ],
            "size": [
              140,
              66
            ],
            "flags": {},
            "order": 14,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "image",
                "name": "image",
                "type": "IMAGE",
                "link": 576
              }
            ],
            "outputs": [
              {
                "localized_name": "width",
                "name": "width",
                "type": "INT",
                "links": [
                  574
                ]
              },
              {
                "localized_name": "height",
                "name": "height",
                "type": "INT",
                "links": [
                  575
                ]
              },
              {
                "localized_name": "batch_size",
                "name": "batch_size",
                "type": "INT",
                "links": null
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "GetImageSize",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": []
          },
          {
            "id": 275,
            "type": "EmptyImage",
            "pos": [
              699.1644412248208,
              6277.115059658317
            ],
            "size": [
              270,
              130
            ],
            "flags": {},
            "order": 13,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "width",
                "name": "width",
                "type": "INT",
                "widget": {
                  "name": "width"
                },
                "link": 574
              },
              {
                "localized_name": "height",
                "name": "height",
                "type": "INT",
                "widget": {
                  "name": "height"
                },
                "link": 575
              }
            ],
            "outputs": [
              {
                "localized_name": "IMAGE",
                "name": "IMAGE",
                "type": "IMAGE",
                "links": [
                  577
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "EmptyImage",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              512,
              512,
              1,
              0
            ]
          },
          {
            "id": 278,
            "type": "GetImageSize",
            "pos": [
              1034.2728423586186,
              6460.194242525011
            ],
            "size": [
              140,
              66
            ],
            "flags": {},
            "order": 16,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "image",
                "name": "image",
                "type": "IMAGE",
                "link": 578
              }
            ],
            "outputs": [
              {
                "localized_name": "width",
                "name": "width",
                "type": "INT",
                "links": [
                  582
                ]
              },
              {
                "localized_name": "height",
                "name": "height",
                "type": "INT",
                "links": [
                  583
                ]
              },
              {
                "localized_name": "batch_size",
                "name": "batch_size",
                "type": "INT",
                "links": null
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "GetImageSize",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": []
          },
          {
            "id": 183,
            "type": "EmptyLTXVLatentVideo",
            "pos": [
              1255.1453465881393,
              6412.2477778068505
            ],
            "size": [
              246.34966275693932,
              130
            ],
            "flags": {
              "collapsed": false
            },
            "order": 4,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "width",
                "name": "width",
                "type": "INT",
                "widget": {
                  "name": "width"
                },
                "link": 582
              },
              {
                "localized_name": "height",
                "name": "height",
                "type": "INT",
                "widget": {
                  "name": "height"
                },
                "link": 583
              },
              {
                "localized_name": "length",
                "name": "length",
                "type": "INT",
                "widget": {
                  "name": "length"
                },
                "link": 375
              }
            ],
            "outputs": [
              {
                "localized_name": "LATENT",
                "name": "LATENT",
                "type": "LATENT",
                "links": [
                  586
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.43",
              "Node name for S&R": "EmptyLTXVLatentVideo",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              736,
              416,
              121,
              1
            ]
          },
          {
            "id": 222,
            "type": "LTXVImgToVideoInplace",
            "pos": [
              1083.6270937248046,
              6209.016766743179
            ],
            "size": [
              392.5712979044981,
              128.5204034965891
            ],
            "flags": {},
            "order": 9,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "vae",
                "name": "vae",
                "type": "VAE",
                "link": 428
              },
              {
                "localized_name": "image",
                "name": "image",
                "type": "IMAGE",
                "link": 585
              },
              {
                "localized_name": "latent",
                "name": "latent",
                "type": "LATENT",
                "link": 586
              }
            ],
            "outputs": [
              {
                "localized_name": "latent",
                "name": "latent",
                "type": "LATENT",
                "links": [
                  426
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.7.0",
              "Node name for S&R": "LTXVImgToVideoInplace",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              1,
              false
            ]
          },
          {
            "id": 182,
            "type": "LTXVEmptyLatentAudio",
            "pos": [
              581.6278660650288,
              6959.616302505887
            ],
            "size": [
              247.383463151142,
              106
            ],
            "flags": {
              "collapsed": false
            },
            "order": 3,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "audio_vae",
                "name": "audio_vae",
                "type": "VAE",
                "link": 429
              },
              {
                "localized_name": "frames_number",
                "name": "frames_number",
                "type": "INT",
                "widget": {
                  "name": "frames_number"
                },
                "link": 371
              },
              {
                "localized_name": "frame_rate",
                "name": "frame_rate",
                "type": "INT",
                "widget": {
                  "name": "frame_rate"
                },
                "link": 607
              }
            ],
            "outputs": [
              {
                "localized_name": "Latent",
                "name": "Latent",
                "type": "LATENT",
                "links": []
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.64",
              "Node name for S&R": "LTXVEmptyLatentAudio",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              121,
              24,
              1
            ]
          },
          {
            "id": 287,
            "type": "VRGDG_LoadAudioSplit_SRTOnly",
            "pos": [
              -256.9401443573618,
              7119.200918809301
            ],
            "size": [
              338.9,
              554
            ],
            "flags": {},
            "order": 19,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "audio",
                "name": "audio",
                "type": "AUDIO",
                "link": 609
              },
              {
                "localized_name": "trigger",
                "name": "trigger",
                "type": "*",
                "link": 610
              },
              {
                "localized_name": "srt_file",
                "name": "srt_file",
                "type": "STRING",
                "widget": {
                  "name": "srt_file"
                },
                "link": 627
              },
              {
                "localized_name": "fixed_duration",
                "name": "fixed_duration",
                "type": "INT",
                "widget": {
                  "name": "fixed_duration"
                },
                "link": 634
              },
              {
                "localized_name": "fps",
                "name": "fps",
                "type": "INT",
                "widget": {
                  "name": "fps"
                },
                "link": 608
              },
              {
                "localized_name": "folder_path",
                "name": "folder_path",
                "type": "STRING",
                "widget": {
                  "name": "folder_path"
                },
                "link": 611
              },
              {
                "localized_name": "enable_auto_queue",
                "name": "enable_auto_queue",
                "type": "BOOLEAN",
                "widget": {
                  "name": "enable_auto_queue"
                },
                "link": 629
              },
              {
                "localized_name": "redo_prompt_number",
                "name": "redo_prompt_number",
                "type": "INT",
                "widget": {
                  "name": "redo_prompt_number"
                },
                "link": 630
              },
              {
                "localized_name": "use_remake_folder",
                "name": "use_remake_folder",
                "type": "BOOLEAN",
                "widget": {
                  "name": "use_remake_folder"
                },
                "link": 635
              },
              {
                "localized_name": "overwrite_mode",
                "name": "overwrite_mode",
                "type": "COMBO",
                "widget": {
                  "name": "overwrite_mode"
                },
                "link": 631
              },
              {
                "localized_name": "tail_loss_frames",
                "name": "tail_loss_frames",
                "type": "INT",
                "widget": {
                  "name": "tail_loss_frames"
                },
                "link": 632
              },
              {
                "localized_name": "pre_frames",
                "name": "pre_frames",
                "type": "INT",
                "widget": {
                  "name": "pre_frames"
                },
                "link": 633
              }
            ],
            "outputs": [
              {
                "localized_name": "meta",
                "name": "meta",
                "type": "DICT",
                "links": null
              },
              {
                "localized_name": "total_duration",
                "name": "total_duration",
                "type": "FLOAT",
                "links": [
                  612
                ]
              },
              {
                "localized_name": "index",
                "name": "index",
                "type": "INT",
                "links": [
                  613
                ]
              },
              {
                "localized_name": "frames_for_ltx",
                "name": "frames_for_ltx",
                "type": "INT",
                "links": [
                  614,
                  626
                ]
              },
              {
                "localized_name": "start_time",
                "name": "start_time",
                "type": "STRING",
                "links": [
                  615
                ]
              },
              {
                "localized_name": "end_time",
                "name": "end_time",
                "type": "STRING",
                "links": [
                  616
                ]
              },
              {
                "localized_name": "instructions",
                "name": "instructions",
                "type": "STRING",
                "links": [
                  617
                ]
              },
              {
                "localized_name": "total_sets",
                "name": "total_sets",
                "type": "INT",
                "links": [
                  618
                ]
              },
              {
                "localized_name": "frames_per_scene",
                "name": "frames_per_scene",
                "type": "INT",
                "links": [
                  619
                ]
              },
              {
                "localized_name": "preroll_frames",
                "name": "preroll_frames",
                "type": "INT",
                "links": [
                  621
                ]
              },
              {
                "localized_name": "audio_meta",
                "name": "audio_meta",
                "type": "DICT",
                "links": null
              },
              {
                "localized_name": "output_folder",
                "name": "output_folder",
                "type": "STRING",
                "links": [
                  622
                ]
              },
              {
                "localized_name": "overwrite_mode",
                "name": "overwrite_mode",
                "type": "STRING",
                "links": [
                  623
                ]
              },
              {
                "localized_name": "audio",
                "name": "audio",
                "type": "AUDIO",
                "links": [
                  624,
                  636
                ]
              },
              {
                "localized_name": "signal_out",
                "name": "signal_out",
                "type": "*",
                "links": null
              }
            ],
            "properties": {
              "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
              "ver": "0b6d046efe93289ded6c1038cabd33642b602f78",
              "Node name for S&R": "VRGDG_LoadAudioSplit_SRTOnly",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              "",
              24,
              24,
              24,
              true,
              0,
              false,
              "backup",
              25,
              50
            ]
          },
          {
            "id": 206,
            "type": "SamplerCustomAdvanced",
            "pos": [
              471.5567792889484,
              7577.294798091485
            ],
            "size": [
              212.38333740234376,
              130
            ],
            "flags": {
              "collapsed": false
            },
            "order": 8,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "noise",
                "name": "noise",
                "type": "NOISE",
                "link": 437
              },
              {
                "localized_name": "guider",
                "name": "guider",
                "type": "GUIDER",
                "link": 384
              },
              {
                "localized_name": "sampler",
                "name": "sampler",
                "type": "SAMPLER",
                "link": 385
              },
              {
                "localized_name": "sigmas",
                "name": "sigmas",
                "type": "SIGMAS",
                "link": 386
              },
              {
                "localized_name": "latent_image",
                "name": "latent_image",
                "type": "LATENT",
                "link": 387
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "LATENT",
                "links": []
              },
              {
                "localized_name": "denoised_output",
                "name": "denoised_output",
                "type": "LATENT",
                "links": [
                  423
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.71",
              "Node name for S&R": "SamplerCustomAdvanced",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 240,
            "type": "LTXVAudioVAEEncode",
            "pos": [
              449.8183291095454,
              7760.790476133398
            ],
            "size": [
              313.3493727825793,
              56.34705382017182
            ],
            "flags": {},
            "order": 10,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "audio",
                "name": "audio",
                "type": "AUDIO",
                "link": 636
              },
              {
                "label": "Audio VAE",
                "localized_name": "audio_vae",
                "name": "audio_vae",
                "type": "VAE",
                "link": 471
              }
            ],
            "outputs": [
              {
                "localized_name": "Audio Latent",
                "name": "Audio Latent",
                "type": "LATENT",
                "links": [
                  465
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.7.0",
              "Node name for S&R": "LTXVAudioVAEEncode",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [],
            "color": "#323",
            "bgcolor": "#535"
          },
          {
            "id": 245,
            "type": "SetLatentNoiseMask",
            "pos": [
              768.047206665142,
              7598.560787675185
            ],
            "size": [
              188.9,
              46
            ],
            "flags": {},
            "order": 11,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "samples",
                "name": "samples",
                "type": "LATENT",
                "link": 465
              },
              {
                "localized_name": "mask",
                "name": "mask",
                "type": "MASK",
                "link": 466
              }
            ],
            "outputs": [
              {
                "localized_name": "LATENT",
                "name": "LATENT",
                "type": "LATENT",
                "links": [
                  468
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.7.0",
              "Node name for S&R": "SetLatentNoiseMask",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [],
            "color": "#323",
            "bgcolor": "#535"
          },
          {
            "id": 246,
            "type": "SolidMask",
            "pos": [
              835.787130834821,
              7743.573624346576
            ],
            "size": [
              270,
              106
            ],
            "flags": {
              "collapsed": false
            },
            "order": 12,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "width",
                "name": "width",
                "type": "INT",
                "widget": {
                  "name": "width"
                },
                "link": 469
              },
              {
                "localized_name": "height",
                "name": "height",
                "type": "INT",
                "widget": {
                  "name": "height"
                },
                "link": 470
              }
            ],
            "outputs": [
              {
                "localized_name": "MASK",
                "name": "MASK",
                "type": "MASK",
                "links": [
                  466
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.7.0",
              "Node name for S&R": "SolidMask",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              0,
              736,
              416
            ]
          },
          {
            "id": 209,
            "type": "ManualSigmas",
            "pos": [
              907.3207853636808,
              7085.210157090039
            ],
            "size": [
              337.9822665203267,
              58
            ],
            "flags": {},
            "order": 1,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "SIGMAS",
                "name": "SIGMAS",
                "type": "SIGMAS",
                "links": [
                  386
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.5.1",
              "Node name for S&R": "ManualSigmas",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "1., 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0"
            ]
          },
          {
            "id": 252,
            "type": "PrimitiveInt",
            "pos": [
              -277.689839268234,
              6960.244638755806
            ],
            "size": [
              270,
              82
            ],
            "flags": {
              "collapsed": true
            },
            "order": 2,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "INT",
                "name": "INT",
                "type": "INT",
                "links": [
                  481,
                  610
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "PrimitiveInt",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              -662848438269308,
              "randomize"
            ]
          }
        ],
        "groups": [
          {
            "id": 16,
            "title": "Group",
            "bounding": [
              552.3618232972951,
              6664.738153937567,
              726.8883117762675,
              688.1911735617432
            ],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
          },
          {
            "id": 17,
            "title": "Group",
            "bounding": [
              -298.5501506531429,
              6880.7997465836825,
              434.0788144909458,
              773.041978448673
            ],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
          },
          {
            "id": 18,
            "title": "Group",
            "bounding": [
              411.078890330525,
              7511.840128992759,
              1328.2528856944039,
              593.1130786757136
            ],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
          },
          {
            "id": 20,
            "title": "Group",
            "bounding": [
              303.05018475947554,
              6135.416766743178,
              1208.4448245856033,
              497.29665960896966
            ],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
          }
        ],
        "links": [
          {
            "id": 384,
            "origin_id": 185,
            "origin_slot": 0,
            "target_id": 206,
            "target_slot": 1,
            "type": "GUIDER"
          },
          {
            "id": 385,
            "origin_id": 186,
            "origin_slot": 0,
            "target_id": 206,
            "target_slot": 2,
            "type": "SAMPLER"
          },
          {
            "id": 386,
            "origin_id": 209,
            "origin_slot": 0,
            "target_id": 206,
            "target_slot": 3,
            "type": "SIGMAS"
          },
          {
            "id": 387,
            "origin_id": 199,
            "origin_slot": 0,
            "target_id": 206,
            "target_slot": 4,
            "type": "LATENT"
          },
          {
            "id": 375,
            "origin_id": 200,
            "origin_slot": 0,
            "target_id": 183,
            "target_slot": 2,
            "type": "INT"
          },
          {
            "id": 371,
            "origin_id": 200,
            "origin_slot": 0,
            "target_id": 182,
            "target_slot": 1,
            "type": "INT"
          },
          {
            "id": 378,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 185,
            "target_slot": 0,
            "type": "MODEL"
          },
          {
            "id": 379,
            "origin_id": -10,
            "origin_slot": 1,
            "target_id": 185,
            "target_slot": 1,
            "type": "CONDITIONING"
          },
          {
            "id": 380,
            "origin_id": -10,
            "origin_slot": 2,
            "target_id": 185,
            "target_slot": 2,
            "type": "CONDITIONING"
          },
          {
            "id": 423,
            "origin_id": 206,
            "origin_slot": 1,
            "target_id": -20,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 426,
            "origin_id": 222,
            "origin_slot": 0,
            "target_id": 199,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 428,
            "origin_id": -10,
            "origin_slot": 3,
            "target_id": 222,
            "target_slot": 0,
            "type": "VAE"
          },
          {
            "id": 429,
            "origin_id": -10,
            "origin_slot": 4,
            "target_id": 182,
            "target_slot": 0,
            "type": "VAE"
          },
          {
            "id": 437,
            "origin_id": -10,
            "origin_slot": 8,
            "target_id": 206,
            "target_slot": 0,
            "type": "NOISE"
          },
          {
            "id": 465,
            "origin_id": 240,
            "origin_slot": 0,
            "target_id": 245,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 466,
            "origin_id": 246,
            "origin_slot": 0,
            "target_id": 245,
            "target_slot": 1,
            "type": "MASK"
          },
          {
            "id": 468,
            "origin_id": 245,
            "origin_slot": 0,
            "target_id": 199,
            "target_slot": 1,
            "type": "LATENT"
          },
          {
            "id": 469,
            "origin_id": -10,
            "origin_slot": 5,
            "target_id": 246,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 470,
            "origin_id": -10,
            "origin_slot": 6,
            "target_id": 246,
            "target_slot": 1,
            "type": "INT"
          },
          {
            "id": 471,
            "origin_id": -10,
            "origin_slot": 4,
            "target_id": 240,
            "target_slot": 1,
            "type": "VAE"
          },
          {
            "id": 574,
            "origin_id": 276,
            "origin_slot": 0,
            "target_id": 275,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 575,
            "origin_id": 276,
            "origin_slot": 1,
            "target_id": 275,
            "target_slot": 1,
            "type": "INT"
          },
          {
            "id": 576,
            "origin_id": 279,
            "origin_slot": 0,
            "target_id": 276,
            "target_slot": 0,
            "type": "IMAGE"
          },
          {
            "id": 577,
            "origin_id": 275,
            "origin_slot": 0,
            "target_id": 277,
            "target_slot": 0,
            "type": "IMAGE"
          },
          {
            "id": 578,
            "origin_id": 277,
            "origin_slot": 0,
            "target_id": 278,
            "target_slot": 0,
            "type": "IMAGE"
          },
          {
            "id": 579,
            "origin_id": -10,
            "origin_slot": 7,
            "target_id": 279,
            "target_slot": 0,
            "type": "IMAGE"
          },
          {
            "id": 580,
            "origin_id": -10,
            "origin_slot": 5,
            "target_id": 279,
            "target_slot": 1,
            "type": "INT"
          },
          {
            "id": 581,
            "origin_id": -10,
            "origin_slot": 6,
            "target_id": 279,
            "target_slot": 2,
            "type": "INT"
          },
          {
            "id": 582,
            "origin_id": 278,
            "origin_slot": 0,
            "target_id": 183,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 583,
            "origin_id": 278,
            "origin_slot": 1,
            "target_id": 183,
            "target_slot": 1,
            "type": "INT"
          },
          {
            "id": 584,
            "origin_id": -10,
            "origin_slot": 7,
            "target_id": 280,
            "target_slot": 0,
            "type": "IMAGE"
          },
          {
            "id": 585,
            "origin_id": 280,
            "origin_slot": 0,
            "target_id": 222,
            "target_slot": 1,
            "type": "IMAGE"
          },
          {
            "id": 586,
            "origin_id": 183,
            "origin_slot": 0,
            "target_id": 222,
            "target_slot": 2,
            "type": "LATENT"
          },
          {
            "id": 607,
            "origin_id": -10,
            "origin_slot": 10,
            "target_id": 182,
            "target_slot": 2,
            "type": "INT"
          },
          {
            "id": 608,
            "origin_id": -10,
            "origin_slot": 10,
            "target_id": 287,
            "target_slot": 4,
            "type": "INT"
          },
          {
            "id": 609,
            "origin_id": -10,
            "origin_slot": 11,
            "target_id": 287,
            "target_slot": 0,
            "type": "AUDIO"
          },
          {
            "id": 610,
            "origin_id": 252,
            "origin_slot": 0,
            "target_id": 287,
            "target_slot": 1,
            "type": "INT"
          },
          {
            "id": 611,
            "origin_id": -10,
            "origin_slot": 9,
            "target_id": 287,
            "target_slot": 5,
            "type": "STRING"
          },
          {
            "id": 612,
            "origin_id": 287,
            "origin_slot": 1,
            "target_id": -20,
            "target_slot": 1,
            "type": "FLOAT"
          },
          {
            "id": 613,
            "origin_id": 287,
            "origin_slot": 2,
            "target_id": -20,
            "target_slot": 2,
            "type": "INT"
          },
          {
            "id": 614,
            "origin_id": 287,
            "origin_slot": 3,
            "target_id": -20,
            "target_slot": 11,
            "type": "INT"
          },
          {
            "id": 615,
            "origin_id": 287,
            "origin_slot": 4,
            "target_id": -20,
            "target_slot": 3,
            "type": "STRING"
          },
          {
            "id": 616,
            "origin_id": 287,
            "origin_slot": 5,
            "target_id": -20,
            "target_slot": 4,
            "type": "STRING"
          },
          {
            "id": 617,
            "origin_id": 287,
            "origin_slot": 6,
            "target_id": -20,
            "target_slot": 5,
            "type": "STRING"
          },
          {
            "id": 618,
            "origin_id": 287,
            "origin_slot": 7,
            "target_id": -20,
            "target_slot": 6,
            "type": "INT"
          },
          {
            "id": 619,
            "origin_id": 287,
            "origin_slot": 8,
            "target_id": -20,
            "target_slot": 7,
            "type": "INT"
          },
          {
            "id": 621,
            "origin_id": 287,
            "origin_slot": 9,
            "target_id": -20,
            "target_slot": 12,
            "type": "INT"
          },
          {
            "id": 622,
            "origin_id": 287,
            "origin_slot": 11,
            "target_id": -20,
            "target_slot": 8,
            "type": "STRING"
          },
          {
            "id": 623,
            "origin_id": 287,
            "origin_slot": 12,
            "target_id": -20,
            "target_slot": 9,
            "type": "STRING"
          },
          {
            "id": 624,
            "origin_id": 287,
            "origin_slot": 13,
            "target_id": -20,
            "target_slot": 10,
            "type": "AUDIO"
          },
          {
            "id": 626,
            "origin_id": 287,
            "origin_slot": 3,
            "target_id": 200,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 627,
            "origin_id": -10,
            "origin_slot": 13,
            "target_id": 287,
            "target_slot": 2,
            "type": "STRING"
          },
          {
            "id": 629,
            "origin_id": -10,
            "origin_slot": 14,
            "target_id": 287,
            "target_slot": 6,
            "type": "BOOLEAN"
          },
          {
            "id": 630,
            "origin_id": -10,
            "origin_slot": 15,
            "target_id": 287,
            "target_slot": 7,
            "type": "INT"
          },
          {
            "id": 631,
            "origin_id": -10,
            "origin_slot": 16,
            "target_id": 287,
            "target_slot": 9,
            "type": "COMBO"
          },
          {
            "id": 632,
            "origin_id": -10,
            "origin_slot": 17,
            "target_id": 287,
            "target_slot": 10,
            "type": "INT"
          },
          {
            "id": 633,
            "origin_id": -10,
            "origin_slot": 18,
            "target_id": 287,
            "target_slot": 11,
            "type": "INT"
          },
          {
            "id": 634,
            "origin_id": -10,
            "origin_slot": 19,
            "target_id": 287,
            "target_slot": 3,
            "type": "INT"
          },
          {
            "id": 635,
            "origin_id": -10,
            "origin_slot": 20,
            "target_id": 287,
            "target_slot": 8,
            "type": "BOOLEAN"
          },
          {
            "id": 636,
            "origin_id": 287,
            "origin_slot": 13,
            "target_id": 240,
            "target_slot": 0,
            "type": "AUDIO"
          }
        ],
        "extra": {
          "workflowRendererVersion": "LG",
          "ue_links": [],
          "links_added_by_ue": []
        }
      },
      {
        "id": "f90e476f-2a4f-488c-89f7-e7f2417460dc",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "Model upscale",
        "inputNode": {
          "id": -10,
          "bounding": [
            1910.8554490535996,
            7820.231673910276,
            124,
            200
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            3019.4107291070345,
            7870.231673910275,
            132,
            60
          ]
        },
        "inputs": [
          {
            "id": "d7bd5fe9-48ed-40cf-84bf-1f673200645d",
            "name": "model",
            "type": "MODEL",
            "linkIds": [
              388
            ],
            "localized_name": "model",
            "pos": [
              2014.8554490535996,
              7840.231673910276
            ]
          },
          {
            "id": "9f8f5168-df83-4cd5-b172-c1b8cd2f0e64",
            "name": "positive",
            "type": "CONDITIONING",
            "linkIds": [
              441
            ],
            "localized_name": "positive",
            "pos": [
              2014.8554490535996,
              7860.231673910276
            ]
          },
          {
            "id": "621b171c-5c0d-4417-a1ff-a33e22b721bc",
            "name": "negative",
            "type": "CONDITIONING",
            "linkIds": [
              442
            ],
            "localized_name": "negative",
            "pos": [
              2014.8554490535996,
              7880.231673910276
            ]
          },
          {
            "id": "a1cfbc21-b475-4dd1-830b-4a8a6410de8f",
            "name": "upscale_model",
            "type": "LATENT_UPSCALE_MODEL",
            "linkIds": [
              406
            ],
            "localized_name": "upscale_model",
            "pos": [
              2014.8554490535996,
              7900.231673910276
            ]
          },
          {
            "id": "b70cf234-7e2a-420f-986c-c919171dae68",
            "name": "vae",
            "type": "VAE",
            "linkIds": [
              411,
              429
            ],
            "localized_name": "vae",
            "pos": [
              2014.8554490535996,
              7920.231673910276
            ]
          },
          {
            "id": "921c41fd-4bcb-4f48-964a-94429b48ab28",
            "name": "image",
            "type": "IMAGE",
            "linkIds": [
              430
            ],
            "pos": [
              2014.8554490535996,
              7940.231673910276
            ]
          },
          {
            "id": "2521db56-7c31-4d91-8b4a-1d578072feda",
            "name": "bypass",
            "type": "BOOLEAN",
            "linkIds": [
              435
            ],
            "label": "bypass image",
            "pos": [
              2014.8554490535996,
              7960.231673910276
            ]
          },
          {
            "id": "3f21c125-7f2e-4d8d-b835-a88921eb9f1b",
            "name": "av_latent",
            "type": "LATENT",
            "linkIds": [
              439
            ],
            "pos": [
              2014.8554490535996,
              7980.231673910276
            ]
          }
        ],
        "outputs": [
          {
            "id": "be4d9eaa-39aa-4e6e-bcbe-6892ad5dbcdb",
            "name": "denoised_output",
            "type": "LATENT",
            "linkIds": [
              428
            ],
            "pos": [
              3039.4107291070345,
              7890.231673910275
            ]
          }
        ],
        "widgets": [],
        "nodes": [
          {
            "id": 188,
            "type": "CFGGuider",
            "pos": [
              2427.0469194048474,
              7735.231797157844
            ],
            "size": [
              270,
              106.66666666666667
            ],
            "flags": {},
            "order": 3,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "model",
                "name": "model",
                "type": "MODEL",
                "link": 388
              },
              {
                "localized_name": "positive",
                "name": "positive",
                "type": "CONDITIONING",
                "link": 443
              },
              {
                "localized_name": "negative",
                "name": "negative",
                "type": "CONDITIONING",
                "link": 444
              }
            ],
            "outputs": [
              {
                "localized_name": "GUIDER",
                "name": "GUIDER",
                "type": "GUIDER",
                "links": [
                  394
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.71",
              "Node name for S&R": "CFGGuider",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              1
            ]
          },
          {
            "id": 208,
            "type": "ManualSigmas",
            "pos": [
              2427.0469194048474,
              8055.231491982058
            ],
            "size": [
              270,
              70
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "SIGMAS",
                "name": "SIGMAS",
                "type": "SIGMAS",
                "links": [
                  396
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.5.1",
              "Node name for S&R": "ManualSigmas",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "0.909375, 0.725, 0.421875, 0.0"
            ]
          },
          {
            "id": 190,
            "type": "LTXVConcatAVLatent",
            "pos": [
              2427.046636592251,
              8185.231623788873
            ],
            "size": [
              270,
              60
            ],
            "flags": {
              "collapsed": false
            },
            "order": 4,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "video_latent",
                "name": "video_latent",
                "type": "LATENT",
                "link": 436
              },
              {
                "localized_name": "audio_latent",
                "name": "audio_latent",
                "type": "LATENT",
                "link": 426
              }
            ],
            "outputs": [
              {
                "localized_name": "latent",
                "name": "latent",
                "type": "LATENT",
                "links": [
                  397
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.5.1",
              "Node name for S&R": "LTXVConcatAVLatent",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 189,
            "type": "RandomNoise",
            "pos": [
              2427.046636592251,
              7585.231724031673
            ],
            "size": [
              270,
              82
            ],
            "flags": {
              "collapsed": false
            },
            "order": 1,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "NOISE",
                "name": "NOISE",
                "type": "NOISE",
                "links": [
                  393
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.71",
              "Node name for S&R": "RandomNoise",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              0,
              "fixed"
            ]
          },
          {
            "id": 207,
            "type": "SamplerCustomAdvanced",
            "pos": [
              2747.0468619195344,
              7595.231671671851
            ],
            "size": [
              212.38333740234376,
              120
            ],
            "flags": {},
            "order": 6,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "noise",
                "name": "noise",
                "type": "NOISE",
                "link": 393
              },
              {
                "localized_name": "guider",
                "name": "guider",
                "type": "GUIDER",
                "link": 394
              },
              {
                "localized_name": "sampler",
                "name": "sampler",
                "type": "SAMPLER",
                "link": 395
              },
              {
                "localized_name": "sigmas",
                "name": "sigmas",
                "type": "SIGMAS",
                "link": 396
              },
              {
                "localized_name": "latent_image",
                "name": "latent_image",
                "type": "LATENT",
                "link": 397
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "LATENT",
                "links": []
              },
              {
                "localized_name": "denoised_output",
                "name": "denoised_output",
                "type": "LATENT",
                "links": [
                  428
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.71",
              "Node name for S&R": "SamplerCustomAdvanced",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 220,
            "type": "LTXVSeparateAVLatent",
            "pos": [
              2090.458557106459,
              7633.744871287468
            ],
            "size": [
              209.76464880859248,
              46
            ],
            "flags": {
              "collapsed": false
            },
            "order": 7,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "av_latent",
                "name": "av_latent",
                "type": "LATENT",
                "link": 439
              }
            ],
            "outputs": [
              {
                "localized_name": "video_latent",
                "name": "video_latent",
                "type": "LATENT",
                "links": [
                  425,
                  445
                ]
              },
              {
                "localized_name": "audio_latent",
                "name": "audio_latent",
                "type": "LATENT",
                "links": [
                  426
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.5.1",
              "Node name for S&R": "LTXVSeparateAVLatent",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 222,
            "type": "LTXVCropGuides",
            "pos": [
              2091.230741466225,
              7722.526253959844
            ],
            "size": [
              210.01878622757786,
              66
            ],
            "flags": {},
            "order": 9,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "positive",
                "name": "positive",
                "type": "CONDITIONING",
                "link": 441
              },
              {
                "localized_name": "negative",
                "name": "negative",
                "type": "CONDITIONING",
                "link": 442
              },
              {
                "localized_name": "latent",
                "name": "latent",
                "type": "LATENT",
                "link": 445
              }
            ],
            "outputs": [
              {
                "localized_name": "positive",
                "name": "positive",
                "type": "CONDITIONING",
                "links": [
                  443
                ]
              },
              {
                "localized_name": "negative",
                "name": "negative",
                "type": "CONDITIONING",
                "links": [
                  444
                ]
              },
              {
                "localized_name": "latent",
                "name": "latent",
                "type": "LATENT",
                "links": [
                  446
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.8.2",
              "Node name for S&R": "LTXVCropGuides",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 192,
            "type": "LTXVLatentUpsampler",
            "pos": [
              2092.6588459112813,
              7830.4928569310405
            ],
            "size": [
              206.41377157626312,
              66
            ],
            "flags": {},
            "order": 5,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "samples",
                "name": "samples",
                "type": "LATENT",
                "link": 446
              },
              {
                "localized_name": "upscale_model",
                "name": "upscale_model",
                "type": "LATENT_UPSCALE_MODEL",
                "link": 406
              },
              {
                "localized_name": "vae",
                "name": "vae",
                "type": "VAE",
                "link": 411
              }
            ],
            "outputs": [
              {
                "localized_name": "LATENT",
                "name": "LATENT",
                "type": "LATENT",
                "links": [
                  433
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.7.0",
              "Node name for S&R": "LTXVLatentUpsampler",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 187,
            "type": "KSamplerSelect",
            "pos": [
              2427.046636592251,
              7905.231569190629
            ],
            "size": [
              270,
              73.99739583333334
            ],
            "flags": {},
            "order": 2,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "SAMPLER",
                "name": "SAMPLER",
                "type": "SAMPLER",
                "links": [
                  395
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.71",
              "Node name for S&R": "KSamplerSelect",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "euler"
            ]
          },
          {
            "id": 221,
            "type": "LTXVImgToVideoInplace",
            "pos": [
              2103.76865190919,
              7962.04881752234
            ],
            "size": [
              230.85524984290942,
              132.7639999189214
            ],
            "flags": {},
            "order": 8,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "vae",
                "name": "vae",
                "type": "VAE",
                "link": 429
              },
              {
                "localized_name": "image",
                "name": "image",
                "type": "IMAGE",
                "link": 430
              },
              {
                "localized_name": "latent",
                "name": "latent",
                "type": "LATENT",
                "link": 433
              },
              {
                "localized_name": "bypass",
                "name": "bypass",
                "type": "BOOLEAN",
                "widget": {
                  "name": "bypass"
                },
                "link": 435
              }
            ],
            "outputs": [
              {
                "localized_name": "latent",
                "name": "latent",
                "type": "LATENT",
                "links": [
                  436
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.7.0",
              "Node name for S&R": "LTXVImgToVideoInplace",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              1,
              false
            ]
          }
        ],
        "groups": [],
        "links": [
          {
            "id": 393,
            "origin_id": 189,
            "origin_slot": 0,
            "target_id": 207,
            "target_slot": 0,
            "type": "NOISE"
          },
          {
            "id": 394,
            "origin_id": 188,
            "origin_slot": 0,
            "target_id": 207,
            "target_slot": 1,
            "type": "GUIDER"
          },
          {
            "id": 395,
            "origin_id": 187,
            "origin_slot": 0,
            "target_id": 207,
            "target_slot": 2,
            "type": "SAMPLER"
          },
          {
            "id": 396,
            "origin_id": 208,
            "origin_slot": 0,
            "target_id": 207,
            "target_slot": 3,
            "type": "SIGMAS"
          },
          {
            "id": 397,
            "origin_id": 190,
            "origin_slot": 0,
            "target_id": 207,
            "target_slot": 4,
            "type": "LATENT"
          },
          {
            "id": 388,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 188,
            "target_slot": 0,
            "type": "MODEL"
          },
          {
            "id": 406,
            "origin_id": -10,
            "origin_slot": 3,
            "target_id": 192,
            "target_slot": 1,
            "type": "LATENT_UPSCALE_MODEL"
          },
          {
            "id": 411,
            "origin_id": -10,
            "origin_slot": 4,
            "target_id": 192,
            "target_slot": 2,
            "type": "VAE"
          },
          {
            "id": 426,
            "origin_id": 220,
            "origin_slot": 1,
            "target_id": 190,
            "target_slot": 1,
            "type": "LATENT"
          },
          {
            "id": 428,
            "origin_id": 207,
            "origin_slot": 1,
            "target_id": -20,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 429,
            "origin_id": -10,
            "origin_slot": 4,
            "target_id": 221,
            "target_slot": 0,
            "type": "VAE"
          },
          {
            "id": 430,
            "origin_id": -10,
            "origin_slot": 5,
            "target_id": 221,
            "target_slot": 1,
            "type": "IMAGE"
          },
          {
            "id": 433,
            "origin_id": 192,
            "origin_slot": 0,
            "target_id": 221,
            "target_slot": 2,
            "type": "LATENT"
          },
          {
            "id": 435,
            "origin_id": -10,
            "origin_slot": 6,
            "target_id": 221,
            "target_slot": 3,
            "type": "BOOLEAN"
          },
          {
            "id": 436,
            "origin_id": 221,
            "origin_slot": 0,
            "target_id": 190,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 439,
            "origin_id": -10,
            "origin_slot": 7,
            "target_id": 220,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 441,
            "origin_id": -10,
            "origin_slot": 1,
            "target_id": 222,
            "target_slot": 0,
            "type": "CONDITIONING"
          },
          {
            "id": 442,
            "origin_id": -10,
            "origin_slot": 2,
            "target_id": 222,
            "target_slot": 1,
            "type": "CONDITIONING"
          },
          {
            "id": 443,
            "origin_id": 222,
            "origin_slot": 0,
            "target_id": 188,
            "target_slot": 1,
            "type": "CONDITIONING"
          },
          {
            "id": 444,
            "origin_id": 222,
            "origin_slot": 1,
            "target_id": 188,
            "target_slot": 2,
            "type": "CONDITIONING"
          },
          {
            "id": 445,
            "origin_id": 220,
            "origin_slot": 0,
            "target_id": 222,
            "target_slot": 2,
            "type": "LATENT"
          },
          {
            "id": 446,
            "origin_id": 222,
            "origin_slot": 2,
            "target_id": 192,
            "target_slot": 0,
            "type": "LATENT"
          }
        ],
        "extra": {
          "workflowRendererVersion": "LG",
          "ue_links": [],
          "links_added_by_ue": []
        }
      },
      {
        "id": "f9b0e4a7-3741-45ee-adfd-065c755d6f56",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "VAE Decode",
        "inputNode": {
          "id": -10,
          "bounding": [
            2440.813669685298,
            7245.414342536243,
            120,
            100
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            2880.7856955996353,
            7255.414342536243,
            120,
            80
          ]
        },
        "inputs": [
          {
            "id": "416729fa-e227-4129-9ec0-94e92e226347",
            "name": "av_latent",
            "type": "LATENT",
            "linkIds": [
              435
            ],
            "localized_name": "av_latent",
            "pos": [
              2540.813669685298,
              7265.414342536243
            ]
          },
          {
            "id": "b6ef07be-d4e2-447e-a12d-a0b62c1d8841",
            "name": "audio_vae",
            "type": "VAE",
            "linkIds": [
              401
            ],
            "localized_name": "audio_vae",
            "pos": [
              2540.813669685298,
              7285.414342536243
            ]
          },
          {
            "id": "cf6393e6-4a6c-49c9-8976-cdfbab9449c3",
            "name": "vae",
            "type": "VAE",
            "linkIds": [
              470,
              472
            ],
            "localized_name": "vae",
            "pos": [
              2540.813669685298,
              7305.414342536243
            ]
          }
        ],
        "outputs": [
          {
            "id": "5c662053-96e6-4c90-a45f-d7e352278028",
            "name": "Audio",
            "type": "AUDIO",
            "linkIds": [
              403
            ],
            "localized_name": "Audio",
            "pos": [
              2900.7856955996353,
              7275.414342536243
            ]
          },
          {
            "id": "f458fa03-c26c-4009-b33b-9066914de813",
            "name": "IMAGE",
            "type": "IMAGE",
            "linkIds": [
              473
            ],
            "localized_name": "IMAGE",
            "pos": [
              2900.7856955996353,
              7295.414342536243
            ]
          }
        ],
        "widgets": [],
        "nodes": [
          {
            "id": 223,
            "type": "LTXVSeparateAVLatent",
            "pos": [
              2619.2607330703445,
              7411.1600352052765
            ],
            "size": [
              209.76464880859248,
              46
            ],
            "flags": {
              "collapsed": false
            },
            "order": 2,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "av_latent",
                "name": "av_latent",
                "type": "LATENT",
                "link": 435
              }
            ],
            "outputs": [
              {
                "localized_name": "video_latent",
                "name": "video_latent",
                "type": "LATENT",
                "links": [
                  471
                ]
              },
              {
                "localized_name": "audio_latent",
                "name": "audio_latent",
                "type": "LATENT",
                "links": [
                  437
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.5.1",
              "Node name for S&R": "LTXVSeparateAVLatent",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 197,
            "type": "LTXVAudioVAEDecode",
            "pos": [
              2620.1012416212575,
              7313.645643950777
            ],
            "size": [
              203.9,
              46
            ],
            "flags": {
              "collapsed": false
            },
            "order": 1,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "samples",
                "name": "samples",
                "type": "LATENT",
                "link": 437
              },
              {
                "localized_name": "audio_vae",
                "name": "audio_vae",
                "type": "VAE",
                "link": 401
              }
            ],
            "outputs": [
              {
                "localized_name": "Audio",
                "name": "Audio",
                "type": "AUDIO",
                "links": [
                  403
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.64",
              "Node name for S&R": "LTXVAudioVAEDecode",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 196,
            "type": "VAEDecodeTiled",
            "pos": [
              2629.8625423976614,
              7104.010170552852
            ],
            "size": [
              210,
              150
            ],
            "flags": {
              "collapsed": false
            },
            "order": 0,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "samples",
                "name": "samples",
                "type": "LATENT",
                "link": 471
              },
              {
                "localized_name": "vae",
                "name": "vae",
                "type": "VAE",
                "link": 472
              }
            ],
            "outputs": [
              {
                "localized_name": "IMAGE",
                "name": "IMAGE",
                "type": "IMAGE",
                "links": [
                  473
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.5.1",
              "Node name for S&R": "VAEDecodeTiled",
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65,
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              1280,
              128,
              32,
              16
            ]
          },
          {
            "id": 237,
            "type": "f7360ec9-585c-4f19-a21b-a1dde6dcb176",
            "pos": [
              2370.3000369111573,
              7051.250415429292
            ],
            "size": [
              140,
              26
            ],
            "flags": {
              "collapsed": false
            },
            "order": 3,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "anything",
                "name": "anything",
                "type": "*",
                "link": 470
              }
            ],
            "outputs": [],
            "properties": {
              "proxyWidgets": [],
              "cnr_id": "comfy-core",
              "ver": "0.8.2",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [],
            "shape": 1
          }
        ],
        "groups": [],
        "links": [
          {
            "id": 437,
            "origin_id": 223,
            "origin_slot": 1,
            "target_id": 197,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 435,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 223,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 401,
            "origin_id": -10,
            "origin_slot": 1,
            "target_id": 197,
            "target_slot": 1,
            "type": "VAE"
          },
          {
            "id": 403,
            "origin_id": 197,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 0,
            "type": "AUDIO"
          },
          {
            "id": 470,
            "origin_id": -10,
            "origin_slot": 2,
            "target_id": 237,
            "target_slot": 0,
            "type": "*"
          },
          {
            "id": 471,
            "origin_id": 223,
            "origin_slot": 0,
            "target_id": 196,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 472,
            "origin_id": -10,
            "origin_slot": 2,
            "target_id": 196,
            "target_slot": 1,
            "type": "VAE"
          },
          {
            "id": 473,
            "origin_id": 196,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 1,
            "type": "IMAGE"
          }
        ],
        "extra": {
          "workflowRendererVersion": "LG",
          "ue_links": [],
          "links_added_by_ue": []
        }
      },
      {
        "id": "10a8d644-7b18-46be-b2d3-53cfa9f21baa",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "New Subgraph",
        "inputNode": {
          "id": -10,
          "bounding": [
            2731.5704118392796,
            7472.327978168421,
            120,
            60
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            3251.6214460407614,
            7482.327978168421,
            120,
            40
          ]
        },
        "inputs": [
          {
            "id": "9bd8b37d-6dfe-47f8-b765-4a78c2ca75c0",
            "name": "anything",
            "type": "*",
            "linkIds": [
              501
            ],
            "localized_name": "anything",
            "shape": 7,
            "pos": [
              55,
              20
            ]
          }
        ],
        "outputs": [],
        "widgets": [],
        "nodes": [
          {
            "id": 266,
            "type": "RAMCleanup",
            "pos": [
              2911.5704118392796,
              7527.152343890556
            ],
            "size": [
              270,
              130
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "anything",
                "name": "anything",
                "shape": 7,
                "type": "*",
                "link": 500
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "*",
                "links": null
              }
            ],
            "properties": {
              "cnr_id": "comfyui_memory_cleanup",
              "ver": "1.1.2",
              "Node name for S&R": "RAMCleanup",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              true,
              true,
              true,
              3
            ]
          },
          {
            "id": 267,
            "type": "VRAMCleanup",
            "pos": [
              2921.6214460407614,
              7377.503612446287
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 1,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "anything",
                "name": "anything",
                "shape": 7,
                "type": "*",
                "link": 501
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "*",
                "links": [
                  500
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfyui_memory_cleanup",
              "ver": "1.1.2",
              "Node name for S&R": "VRAMCleanup",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              false,
              true
            ]
          }
        ],
        "groups": [],
        "links": [
          {
            "id": 500,
            "origin_id": 267,
            "origin_slot": 0,
            "target_id": 266,
            "target_slot": 0,
            "type": "*"
          },
          {
            "id": 501,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 267,
            "target_slot": 0,
            "type": "LATENT"
          }
        ],
        "extra": {
          "ue_links": [],
          "links_added_by_ue": [],
          "workflowRendererVersion": "LG"
        }
      },
      {
        "id": "acbce015-ba7f-49d9-9d32-4a29c248e609",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "New Subgraph",
        "inputNode": {
          "id": -10,
          "bounding": [
            2366.0782590581653,
            7767.675172334978,
            120,
            60
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            2886.129293259647,
            7777.675172334978,
            120,
            40
          ]
        },
        "inputs": [
          {
            "id": "9eefe0c5-fee0-4c01-b474-11d8792168e4",
            "name": "anything",
            "type": "*",
            "linkIds": [
              499
            ],
            "localized_name": "anything",
            "shape": 7,
            "pos": [
              55,
              20
            ]
          }
        ],
        "outputs": [],
        "widgets": [],
        "nodes": [
          {
            "id": 264,
            "type": "RAMCleanup",
            "pos": [
              2546.0782590581653,
              7822.499538057113
            ],
            "size": [
              270,
              130
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "anything",
                "name": "anything",
                "shape": 7,
                "type": "*",
                "link": 498
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "*",
                "links": null
              }
            ],
            "properties": {
              "cnr_id": "comfyui_memory_cleanup",
              "ver": "1.1.2",
              "Node name for S&R": "RAMCleanup",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              true,
              true,
              true,
              3
            ]
          },
          {
            "id": 265,
            "type": "VRAMCleanup",
            "pos": [
              2556.129293259647,
              7672.850806612843
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 1,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "anything",
                "name": "anything",
                "shape": 7,
                "type": "*",
                "link": 499
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "*",
                "links": [
                  498
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfyui_memory_cleanup",
              "ver": "1.1.2",
              "Node name for S&R": "VRAMCleanup",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              false,
              true
            ]
          }
        ],
        "groups": [],
        "links": [
          {
            "id": 498,
            "origin_id": 265,
            "origin_slot": 0,
            "target_id": 264,
            "target_slot": 0,
            "type": "*"
          },
          {
            "id": 499,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 265,
            "target_slot": 0,
            "type": "LATENT"
          }
        ],
        "extra": {
          "ue_links": [],
          "links_added_by_ue": [],
          "workflowRendererVersion": "LG"
        }
      },
      {
        "id": "7ab38c03-20ca-4807-90e3-a779e4478032",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "models",
        "inputNode": {
          "id": -10,
          "bounding": [
            865.6701408718844,
            6232.811350791974,
            243,
            160
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            2182.07222690524,
            6238.630030074028,
            194,
            140
          ]
        },
        "inputs": [
          {
            "id": "9b6ab5ad-972e-4dba-964c-f654e937dce3",
            "name": "unet_name",
            "type": "COMBO",
            "linkIds": [
              507
            ],
            "label": "Unet Loader (GGUF)",
            "pos": [
              1088.6701408718845,
              6252.811350791974
            ]
          },
          {
            "id": "196768aa-3ac7-44ff-901d-4e8fd4d05873",
            "name": "vae_name",
            "type": "COMBO",
            "linkIds": [
              508
            ],
            "label": "Video-VAELoader KJ Vae_name",
            "pos": [
              1088.6701408718845,
              6272.811350791974
            ]
          },
          {
            "id": "995200ed-55ef-4d8e-ad2c-6dba921c7252",
            "name": "clip_name1",
            "type": "COMBO",
            "linkIds": [
              509
            ],
            "label": "DualClipLoader (GGUF) clip name1",
            "pos": [
              1088.6701408718845,
              6292.811350791974
            ]
          },
          {
            "id": "b2627535-bd8e-4b87-ac9b-a59daa369e59",
            "name": "clip_name2",
            "type": "COMBO",
            "linkIds": [
              510
            ],
            "label": "DualClipLoader (GGUF) Clip name 2",
            "pos": [
              1088.6701408718845,
              6312.811350791974
            ]
          },
          {
            "id": "66601612-3af9-4772-9e83-e3a756a27074",
            "name": "model_name",
            "type": "COMBO",
            "linkIds": [
              511
            ],
            "label": "Load Latent Upscaler Model name",
            "pos": [
              1088.6701408718845,
              6332.811350791974
            ]
          },
          {
            "id": "08314c6b-a1d0-48bd-aea0-1777c8c09fa4",
            "name": "vae_name_1",
            "type": "COMBO",
            "linkIds": [
              512
            ],
            "label": "Audio-VAE Loader KJ vae name",
            "pos": [
              1088.6701408718845,
              6352.811350791974
            ]
          }
        ],
        "outputs": [
          {
            "id": "815107e9-c487-436c-b29a-575d4ddcf9ee",
            "name": "VAE",
            "type": "VAE",
            "linkIds": [
              489,
              490,
              491
            ],
            "localized_name": "VAE",
            "pos": [
              2202.07222690524,
              6258.630030074028
            ]
          },
          {
            "id": "d8006eb6-6dfe-49d0-87f2-4aae6a6307c2",
            "name": "CLIP",
            "type": "CLIP",
            "linkIds": [
              456
            ],
            "localized_name": "CLIP",
            "pos": [
              2202.07222690524,
              6278.630030074028
            ]
          },
          {
            "id": "fd150e38-f405-4dd6-9221-2dcc351eb00f",
            "name": "LATENT_UPSCALE_MODEL",
            "type": "LATENT_UPSCALE_MODEL",
            "linkIds": [
              423
            ],
            "localized_name": "LATENT_UPSCALE_MODEL",
            "pos": [
              2202.07222690524,
              6298.630030074028
            ]
          },
          {
            "id": "cebb637c-f256-40a6-9c34-1929e47ae282",
            "name": "VAE_1",
            "type": "VAE",
            "linkIds": [
              487,
              488
            ],
            "localized_name": "VAE_1",
            "label": "Audio_VAE",
            "pos": [
              2202.07222690524,
              6318.630030074028
            ]
          },
          {
            "id": "94e9dc02-06d2-404f-b7f1-3e211726f9c5",
            "name": "MODEL",
            "type": "MODEL",
            "linkIds": [
              1281
            ],
            "localized_name": "MODEL",
            "pos": [
              2202.07222690524,
              6338.630030074028
            ]
          }
        ],
        "widgets": [],
        "nodes": [
          {
            "id": 216,
            "type": "DualCLIPLoaderGGUF",
            "pos": [
              1274.4133443520157,
              6301.8199752836035
            ],
            "size": [
              586.5424693175662,
              128.7528824811152
            ],
            "flags": {},
            "order": 3,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "clip_name1",
                "name": "clip_name1",
                "type": "COMBO",
                "widget": {
                  "name": "clip_name1"
                },
                "link": 509
              },
              {
                "localized_name": "clip_name2",
                "name": "clip_name2",
                "type": "COMBO",
                "widget": {
                  "name": "clip_name2"
                },
                "link": 510
              }
            ],
            "outputs": [
              {
                "localized_name": "CLIP",
                "name": "CLIP",
                "type": "CLIP",
                "links": [
                  456
                ]
              }
            ],
            "properties": {
              "cnr_id": "ComfyUI-GGUF",
              "ver": "6ea2651e7df66d7585f6ffee804b20e92fb38b8a",
              "Node name for S&R": "DualCLIPLoaderGGUF",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "gemma-3-12b-it-abliterated-sikaworld-high-fidelity-edition.safetensors",
              "ltx-2.3_text_projection_bf16.safetensors",
              "ltxv"
            ]
          },
          {
            "id": 211,
            "type": "LatentUpscaleModelLoader",
            "pos": [
              1284.2459240002122,
              6486.556209906927
            ],
            "size": [
              596.7000073134823,
              58
            ],
            "flags": {},
            "order": 1,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "model_name",
                "name": "model_name",
                "type": "COMBO",
                "widget": {
                  "name": "model_name"
                },
                "link": 511
              }
            ],
            "outputs": [
              {
                "localized_name": "LATENT_UPSCALE_MODEL",
                "name": "LATENT_UPSCALE_MODEL",
                "type": "LATENT_UPSCALE_MODEL",
                "links": [
                  423
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.7.0",
              "Node name for S&R": "LatentUpscaleModelLoader",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              },
              "models": [
                {
                  "name": "ltx-2-spatial-upscaler-x2-1.0.safetensors",
                  "url": "https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors",
                  "directory": "latent_upscale_models"
                }
              ],
              "enableTabs": false,
              "tabWidth": 65,
              "tabXOffset": 10,
              "hasSecondTab": false,
              "secondTabText": "Send Back",
              "secondTabOffset": 80,
              "secondTabWidth": 65
            },
            "widgets_values": [
              "ltx-2.3-spatial-upscaler-x2-1.1.safetensors"
            ]
          },
          {
            "id": 254,
            "type": "VAELoaderKJ",
            "pos": [
              1290.8426889721734,
              6604.413169865589
            ],
            "size": [
              540.7081670707773,
              114.66776475471124
            ],
            "flags": {},
            "order": 4,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "vae_name",
                "name": "vae_name",
                "type": "COMBO",
                "widget": {
                  "name": "vae_name"
                },
                "link": 512
              }
            ],
            "outputs": [
              {
                "localized_name": "VAE",
                "name": "VAE",
                "type": "VAE",
                "links": [
                  487,
                  488
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfyui-kjnodes",
              "ver": "37bda1000e75e5649c224b0b4a8a6f57093ef925",
              "Node name for S&R": "VAELoaderKJ",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "LTX23_audio_vae_bf16.safetensors",
              "main_device",
              "bf16"
            ]
          },
          {
            "id": 256,
            "type": "VAELoaderKJ",
            "pos": [
              1271.7177911920837,
              6136.782316466455
            ],
            "size": [
              576.0769077925193,
              107.0834705943389
            ],
            "flags": {},
            "order": 5,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "vae_name",
                "name": "vae_name",
                "type": "COMBO",
                "widget": {
                  "name": "vae_name"
                },
                "link": 508
              }
            ],
            "outputs": [
              {
                "localized_name": "VAE",
                "name": "VAE",
                "type": "VAE",
                "links": [
                  489,
                  490,
                  491
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfyui-kjnodes",
              "ver": "37bda1000e75e5649c224b0b4a8a6f57093ef925",
              "Node name for S&R": "VAELoaderKJ",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "LTX23_video_vae_bf16.safetensors",
              "main_device",
              "bf16"
            ]
          },
          {
            "id": 215,
            "type": "UnetLoaderGGUF",
            "pos": [
              1267.91104308287,
              6013.814944196909
            ],
            "size": [
              603.1928365559074,
              58
            ],
            "flags": {},
            "order": 2,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "unet_name",
                "name": "unet_name",
                "type": "COMBO",
                "widget": {
                  "name": "unet_name"
                },
                "link": 507
              }
            ],
            "outputs": [
              {
                "localized_name": "MODEL",
                "name": "MODEL",
                "type": "MODEL",
                "links": [
                  1280
                ]
              }
            ],
            "properties": {
              "cnr_id": "ComfyUI-GGUF",
              "ver": "6ea2651e7df66d7585f6ffee804b20e92fb38b8a",
              "Node name for S&R": "UnetLoaderGGUF",
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "LTX-2.3-22B-distilled-1.1-Q6_K.gguf"
            ]
          },
          {
            "id": 827,
            "type": "MarkdownNote",
            "pos": [
              2015.288534709863,
              5804.170464939171
            ],
            "size": [
              335.52526975966555,
              113.46780888057606
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [],
            "outputs": [],
            "properties": {
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "# This blonde character lora can be found [HERE](https://huggingface.co/vrgamedevgirl84/BlondeFemaleZimageLora/blob/main/ltx_BlondWomeon1750.comfy.safetensors)\nOr use your own. "
            ],
            "color": "#432",
            "bgcolor": "#653"
          },
          {
            "id": 816,
            "type": "LoraLoaderModelOnly",
            "pos": [
              1937.6932360295932,
              5977.728160709628
            ],
            "size": [
              449.60662934168704,
              105.94755057889142
            ],
            "flags": {},
            "order": 6,
            "mode": 4,
            "inputs": [
              {
                "localized_name": "model",
                "name": "model",
                "type": "MODEL",
                "link": 1280
              }
            ],
            "outputs": [
              {
                "localized_name": "MODEL",
                "name": "MODEL",
                "type": "MODEL",
                "links": [
                  1281
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.16.2",
              "Node name for S&R": "LoraLoaderModelOnly",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              "LTX\\ltx_BlondWomeon1750.comfy.safetensors",
              1
            ]
          }
        ],
        "groups": [
          {
            "id": 1,
            "title": "Group",
            "bounding": [
              1257.91104308287,
              5773.2960780698495,
              633.0348882308244,
              955.7848565504506
            ],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
          }
        ],
        "links": [
          {
            "id": 489,
            "origin_id": 256,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 0,
            "type": "VAE"
          },
          {
            "id": 490,
            "origin_id": 256,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 0,
            "type": "VAE"
          },
          {
            "id": 491,
            "origin_id": 256,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 0,
            "type": "VAE"
          },
          {
            "id": 456,
            "origin_id": 216,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 1,
            "type": "CLIP"
          },
          {
            "id": 423,
            "origin_id": 211,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 2,
            "type": "LATENT_UPSCALE_MODEL"
          },
          {
            "id": 487,
            "origin_id": 254,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 3,
            "type": "VAE"
          },
          {
            "id": 488,
            "origin_id": 254,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 3,
            "type": "VAE"
          },
          {
            "id": 507,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 215,
            "target_slot": 0,
            "type": "COMBO"
          },
          {
            "id": 508,
            "origin_id": -10,
            "origin_slot": 1,
            "target_id": 256,
            "target_slot": 0,
            "type": "COMBO"
          },
          {
            "id": 509,
            "origin_id": -10,
            "origin_slot": 2,
            "target_id": 216,
            "target_slot": 0,
            "type": "COMBO"
          },
          {
            "id": 510,
            "origin_id": -10,
            "origin_slot": 3,
            "target_id": 216,
            "target_slot": 1,
            "type": "COMBO"
          },
          {
            "id": 511,
            "origin_id": -10,
            "origin_slot": 4,
            "target_id": 211,
            "target_slot": 0,
            "type": "COMBO"
          },
          {
            "id": 512,
            "origin_id": -10,
            "origin_slot": 5,
            "target_id": 254,
            "target_slot": 0,
            "type": "COMBO"
          },
          {
            "id": 1280,
            "origin_id": 215,
            "origin_slot": 0,
            "target_id": 816,
            "target_slot": 0,
            "type": "MODEL"
          },
          {
            "id": 1281,
            "origin_id": 816,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 4,
            "type": "MODEL"
          }
        ],
        "extra": {
          "ue_links": [],
          "links_added_by_ue": [],
          "workflowRendererVersion": "LG"
        }
      },
      {
        "id": "f7360ec9-585c-4f19-a21b-a1dde6dcb176",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "New Subgraph",
        "inputNode": {
          "id": -10,
          "bounding": [
            2731.5704118392796,
            7472.327978168421,
            120,
            60
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            3251.6214460407614,
            7482.327978168421,
            120,
            40
          ]
        },
        "inputs": [
          {
            "id": "9bd8b37d-6dfe-47f8-b765-4a78c2ca75c0",
            "name": "anything",
            "type": "*",
            "linkIds": [
              501
            ],
            "localized_name": "anything",
            "shape": 7,
            "pos": [
              55,
              20
            ]
          }
        ],
        "outputs": [],
        "widgets": [],
        "nodes": [
          {
            "id": 266,
            "type": "RAMCleanup",
            "pos": [
              2911.5704118392796,
              7527.152343890556
            ],
            "size": [
              270,
              130
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "anything",
                "name": "anything",
                "shape": 7,
                "type": "*",
                "link": 500
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "*",
                "links": null
              }
            ],
            "properties": {
              "cnr_id": "comfyui_memory_cleanup",
              "ver": "1.1.2",
              "Node name for S&R": "RAMCleanup",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              true,
              true,
              true,
              3
            ]
          },
          {
            "id": 267,
            "type": "VRAMCleanup",
            "pos": [
              2921.6214460407614,
              7377.503612446287
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 1,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "anything",
                "name": "anything",
                "shape": 7,
                "type": "*",
                "link": 501
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "*",
                "links": [
                  500
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfyui_memory_cleanup",
              "ver": "1.1.2",
              "Node name for S&R": "VRAMCleanup",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              false,
              true
            ]
          }
        ],
        "groups": [],
        "links": [
          {
            "id": 500,
            "origin_id": 267,
            "origin_slot": 0,
            "target_id": 266,
            "target_slot": 0,
            "type": "*"
          },
          {
            "id": 501,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 267,
            "target_slot": 0,
            "type": "LATENT"
          }
        ],
        "extra": {
          "ue_links": [],
          "links_added_by_ue": [],
          "workflowRendererVersion": "LG"
        }
      },
      {
        "id": "161cba0f-5aad-4f66-9635-0eff423013f8",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "Auto Get folder name and audio file",
        "inputNode": {
          "id": -10,
          "bounding": [
            2570.894808773301,
            6739.120469013189,
            120,
            40
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            3174.9332626183077,
            6696.531102686386,
            127,
            80
          ]
        },
        "inputs": [],
        "outputs": [
          {
            "id": "7a431017-5c7b-4225-8a04-651330f56eea",
            "name": "audio_file_path",
            "type": "STRING",
            "linkIds": [
              43
            ],
            "pos": [
              3194.9332626183077,
              6716.531102686386
            ]
          },
          {
            "id": "d246641f-0ecf-474c-9f66-c42e0575e3db",
            "name": "result_text",
            "type": "STRING",
            "linkIds": [
              44
            ],
            "label": "for folder name",
            "pos": [
              3194.9332626183077,
              6736.531102686386
            ]
          }
        ],
        "widgets": [],
        "nodes": [
          {
            "id": 35,
            "type": "PrimitiveInt",
            "pos": [
              2754.8147238249067,
              6662.173944786737
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "INT",
                "name": "INT",
                "type": "INT",
                "links": [
                  42
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.10.0",
              "Node name for S&R": "PrimitiveInt",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              -1089558275781909,
              "randomize"
            ]
          },
          {
            "id": 39,
            "type": "VRGDG_LoadAudioFilePath",
            "pos": [
              2775.6214226607162,
              6812.676329113973
            ],
            "size": [
              277.9,
              78
            ],
            "flags": {},
            "order": 1,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "refresh",
                "name": "refresh",
                "type": "INT",
                "widget": {
                  "name": "refresh"
                },
                "link": 42
              }
            ],
            "outputs": [
              {
                "localized_name": "audio_file_path",
                "name": "audio_file_path",
                "type": "STRING",
                "links": [
                  43
                ]
              },
              {
                "localized_name": "audio_file_name",
                "name": "audio_file_name",
                "type": "STRING",
                "links": [
                  44
                ]
              }
            ],
            "properties": {
              "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
              "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
              "Node name for S&R": "VRGDG_LoadAudioFilePath",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              0
            ]
          }
        ],
        "groups": [],
        "links": [
          {
            "id": 42,
            "origin_id": 35,
            "origin_slot": 0,
            "target_id": 39,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 43,
            "origin_id": 39,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 0,
            "type": "STRING"
          },
          {
            "id": 44,
            "origin_id": 39,
            "origin_slot": 1,
            "target_id": -20,
            "target_slot": 1,
            "type": "STRING"
          }
        ],
        "extra": {
          "workflowRendererVersion": "LG",
          "ue_links": [],
          "links_added_by_ue": []
        }
      },
      {
        "id": "be185d6e-1771-4b9a-a682-a726b24d06e2",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "Settings",
        "inputNode": {
          "id": -10,
          "bounding": [
            -984.5618218672935,
            4769.364952318225,
            193,
            140
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            -212.198718074348,
            5219.179291398261,
            188,
            220
          ]
        },
        "inputs": [
          {
            "id": "f35799f0-c95a-4e7c-8511-48ba923820f5",
            "name": "value",
            "type": "INT",
            "linkIds": [
              1149
            ],
            "label": "Frames Per Second",
            "pos": [
              -811.5618218672935,
              4789.364952318225
            ]
          },
          {
            "id": "1224d539-a7ed-4562-9a18-66e47ce43e7c",
            "name": "value_1",
            "type": "INT",
            "linkIds": [
              1150
            ],
            "label": "Width",
            "pos": [
              -811.5618218672935,
              4809.364952318225
            ]
          },
          {
            "id": "943ce99c-e0eb-4b07-b226-2a4ca2dc9033",
            "name": "value_2",
            "type": "INT",
            "linkIds": [
              1151
            ],
            "label": "Height",
            "pos": [
              -811.5618218672935,
              4829.364952318225
            ]
          },
          {
            "id": "9e5aa06a-e603-4df5-b297-7884b0b42048",
            "name": "value_3",
            "type": "INT",
            "linkIds": [
              1152
            ],
            "label": "Seed",
            "pos": [
              -811.5618218672935,
              4849.364952318225
            ]
          },
          {
            "id": "63865cb9-ee57-40cc-943e-70469abd8eed",
            "name": "value_4",
            "type": "INT",
            "linkIds": [
              1153
            ],
            "label": "Scene Duration when fixed",
            "pos": [
              -811.5618218672935,
              4869.364952318225
            ]
          }
        ],
        "outputs": [
          {
            "id": "7bee9444-575b-4569-9f12-92c6270ed673",
            "name": "INT_1",
            "type": "INT",
            "linkIds": [
              718
            ],
            "localized_name": "INT_1",
            "label": "width",
            "pos": [
              -192.198718074348,
              5239.179291398261
            ]
          },
          {
            "id": "35abe493-521b-4768-891a-8d14d180d6c3",
            "name": "INT_2",
            "type": "INT",
            "linkIds": [
              719
            ],
            "localized_name": "INT_2",
            "label": "height",
            "pos": [
              -192.198718074348,
              5259.179291398261
            ]
          },
          {
            "id": "e5a907fb-1a9e-4b63-b7fd-e4c2803410cf",
            "name": "INT_3",
            "type": "INT",
            "linkIds": [
              734
            ],
            "localized_name": "INT_3",
            "label": "seed",
            "pos": [
              -192.198718074348,
              5279.179291398261
            ]
          },
          {
            "id": "206158f7-9875-4b59-91af-9591e0bbcb99",
            "name": "result_text",
            "type": "STRING",
            "linkIds": [
              1131
            ],
            "label": "for folder name",
            "pos": [
              -192.198718074348,
              5299.179291398261
            ]
          },
          {
            "id": "426ef614-ca15-45f1-84bc-d73d4e273f2a",
            "name": "audio",
            "type": "AUDIO",
            "linkIds": [
              1211
            ],
            "localized_name": "audio",
            "pos": [
              -192.198718074348,
              5319.179291398261
            ]
          },
          {
            "id": "8d5d0b55-1d66-4d3f-a708-981ce2423608",
            "name": "INT_4",
            "type": "INT",
            "linkIds": [
              720,
              729
            ],
            "localized_name": "INT_4",
            "label": "frames per second",
            "pos": [
              -192.198718074348,
              5339.179291398261
            ]
          },
          {
            "id": "1326f441-8758-472e-8a95-cd78d8fda7d0",
            "name": "STRING",
            "type": "STRING",
            "linkIds": [
              1157
            ],
            "label": "Folder Name",
            "pos": [
              -192.198718074348,
              5359.179291398261
            ]
          },
          {
            "id": "d5493493-e05b-4c40-b17f-4592c98564bf",
            "name": "STRING_1",
            "type": "STRING",
            "linkIds": [
              1156
            ],
            "label": "Audio File Path",
            "pos": [
              -192.198718074348,
              5379.179291398261
            ]
          },
          {
            "id": "b5d93dca-a07a-46f8-ba25-ae8f6d4a38dd",
            "name": "INT",
            "type": "INT",
            "linkIds": [
              1233
            ],
            "label": "SceneDurationWhenFixed",
            "pos": [
              -192.198718074348,
              5399.179291398261
            ]
          }
        ],
        "widgets": [],
        "nodes": [
          {
            "id": 425,
            "type": "PrimitiveInt",
            "pos": [
              -609.9774875010714,
              5000.175972586212
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 3,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "value",
                "name": "value",
                "type": "INT",
                "widget": {
                  "name": "value"
                },
                "link": 1150
              }
            ],
            "outputs": [
              {
                "localized_name": "INT",
                "name": "INT",
                "type": "INT",
                "links": [
                  718
                ]
              }
            ],
            "title": "Width",
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "PrimitiveInt",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              1920,
              "fixed"
            ],
            "color": "#432",
            "bgcolor": "#653",
            "shape": 1
          },
          {
            "id": 426,
            "type": "PrimitiveInt",
            "pos": [
              -600.4713444571164,
              5172.8276987385125
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 4,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "value",
                "name": "value",
                "type": "INT",
                "widget": {
                  "name": "value"
                },
                "link": 1151
              }
            ],
            "outputs": [
              {
                "localized_name": "INT",
                "name": "INT",
                "type": "INT",
                "links": [
                  719
                ]
              }
            ],
            "title": "Height",
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "PrimitiveInt",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              1080,
              "fixed"
            ],
            "color": "#432",
            "bgcolor": "#653",
            "shape": 1
          },
          {
            "id": 449,
            "type": "PrimitiveInt",
            "pos": [
              -644.4794036706323,
              5314.854401638765
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 5,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "value",
                "name": "value",
                "type": "INT",
                "widget": {
                  "name": "value"
                },
                "link": 1152
              }
            ],
            "outputs": [
              {
                "localized_name": "INT",
                "name": "INT",
                "type": "INT",
                "links": [
                  734
                ]
              }
            ],
            "title": "Seed",
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "PrimitiveInt",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              123456789,
              "fixed"
            ],
            "color": "#332922",
            "bgcolor": "#593930",
            "shape": 1
          },
          {
            "id": 424,
            "type": "PrimitiveInt",
            "pos": [
              -644.1463497516298,
              4769.698361024755
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 2,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "value",
                "name": "value",
                "type": "INT",
                "widget": {
                  "name": "value"
                },
                "link": 1149
              }
            ],
            "outputs": [
              {
                "localized_name": "INT",
                "name": "INT",
                "type": "INT",
                "links": [
                  720,
                  729
                ]
              }
            ],
            "title": "Frames Per Second",
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "PrimitiveInt",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              24,
              "fixed"
            ],
            "color": "#323",
            "bgcolor": "#535",
            "shape": 1
          },
          {
            "id": 725,
            "type": "161cba0f-5aad-4f66-9635-0eff423013f8",
            "pos": [
              -1064.2385652477356,
              5404.025782727175
            ],
            "size": [
              316.64118768523963,
              46
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "name": "audio_file_path",
                "type": "STRING",
                "links": [
                  1134,
                  1156
                ]
              },
              {
                "label": "for folder name",
                "name": "result_text",
                "type": "STRING",
                "links": [
                  1131,
                  1157
                ]
              }
            ],
            "properties": {
              "proxyWidgets": [],
              "cnr_id": "comfy-core",
              "ver": "0.10.0",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [],
            "color": "#323",
            "bgcolor": "#535"
          },
          {
            "id": 691,
            "type": "VHS_LoadAudio",
            "pos": [
              -600.586737525454,
              5531.5537792411815
            ],
            "size": [
              234,
              180
            ],
            "flags": {},
            "order": 1,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "audio_file",
                "name": "audio_file",
                "type": "STRING",
                "widget": {
                  "name": "audio_file"
                },
                "link": 1134
              }
            ],
            "outputs": [
              {
                "localized_name": "audio",
                "name": "audio",
                "type": "AUDIO",
                "links": [
                  1211
                ]
              },
              {
                "localized_name": "duration",
                "name": "duration",
                "type": "FLOAT",
                "links": null
              }
            ],
            "properties": {
              "cnr_id": "comfyui-videohelpersuite",
              "ver": "1.7.9",
              "Node name for S&R": "VHS_LoadAudio",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": {
              "audio_file": "input/",
              "seek_seconds": 0,
              "duration": 0,
              "audiopreview": {
                "params": {
                  "start_time": 0,
                  "duration": 0
                }
              }
            },
            "color": "#223",
            "bgcolor": "#335"
          },
          {
            "id": 551,
            "type": "PrimitiveInt",
            "pos": [
              -247.4626208108056,
              4825.165161797112
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 6,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "value",
                "name": "value",
                "type": "INT",
                "widget": {
                  "name": "value"
                },
                "link": 1153
              }
            ],
            "outputs": [
              {
                "localized_name": "INT",
                "name": "INT",
                "type": "INT",
                "links": [
                  1233
                ]
              }
            ],
            "title": "scene duration when fixed",
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.9.2",
              "Node name for S&R": "PrimitiveInt",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              0,
              "fixed"
            ],
            "color": "#323",
            "bgcolor": "#535",
            "shape": 1
          }
        ],
        "groups": [],
        "links": [
          {
            "id": 1134,
            "origin_id": 725,
            "origin_slot": 0,
            "target_id": 691,
            "target_slot": 0,
            "type": "STRING"
          },
          {
            "id": 718,
            "origin_id": 425,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 719,
            "origin_id": 426,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 1,
            "type": "INT"
          },
          {
            "id": 734,
            "origin_id": 449,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 2,
            "type": "INT"
          },
          {
            "id": 1131,
            "origin_id": 725,
            "origin_slot": 1,
            "target_id": -20,
            "target_slot": 3,
            "type": "STRING"
          },
          {
            "id": 720,
            "origin_id": 424,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 5,
            "type": "INT"
          },
          {
            "id": 729,
            "origin_id": 424,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 5,
            "type": "INT"
          },
          {
            "id": 1149,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 424,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 1150,
            "origin_id": -10,
            "origin_slot": 1,
            "target_id": 425,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 1151,
            "origin_id": -10,
            "origin_slot": 2,
            "target_id": 426,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 1152,
            "origin_id": -10,
            "origin_slot": 3,
            "target_id": 449,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 1153,
            "origin_id": -10,
            "origin_slot": 4,
            "target_id": 551,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 1156,
            "origin_id": 725,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 7,
            "type": "STRING"
          },
          {
            "id": 1157,
            "origin_id": 725,
            "origin_slot": 1,
            "target_id": -20,
            "target_slot": 6,
            "type": "STRING"
          },
          {
            "id": 1211,
            "origin_id": 691,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 4,
            "type": "AUDIO"
          },
          {
            "id": 1233,
            "origin_id": 551,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 8,
            "type": "INT"
          }
        ],
        "extra": {
          "workflowRendererVersion": "LG",
          "ue_links": [],
          "links_added_by_ue": []
        }
      },
      {
        "id": "3cae606b-5e3e-4046-8c9f-8fffd361c513",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "Z-Image",
        "inputNode": {
          "id": -10,
          "bounding": [
            -219.8663686894322,
            -705.9977743396407,
            127,
            240
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            1740.8874614635452,
            -742.7013262850722,
            120,
            60
          ]
        },
        "inputs": [
          {
            "id": "d57da5ba-eaed-4402-80d8-d3b56f6f7546",
            "name": "text",
            "type": "STRING",
            "linkIds": [
              147
            ],
            "pos": [
              -112.86636868943219,
              -685.9977743396407
            ]
          },
          {
            "id": "46e37f8f-0a6f-4e6c-b786-dba4e813185d",
            "name": "text_1",
            "type": "STRING",
            "linkIds": [
              148
            ],
            "pos": [
              -112.86636868943219,
              -665.9977743396407
            ]
          },
          {
            "id": "214176cd-4db7-46b6-83e5-e1c908976d9b",
            "name": "seed",
            "type": "INT",
            "linkIds": [
              219
            ],
            "pos": [
              -112.86636868943219,
              -645.9977743396407
            ]
          },
          {
            "id": "1cc91a6b-ed4a-4687-aa4a-c3a6efe34358",
            "name": "width",
            "type": "INT",
            "linkIds": [
              328
            ],
            "pos": [
              -112.86636868943219,
              -625.9977743396407
            ]
          },
          {
            "id": "a5436f34-7b3f-49cd-914c-87a5f6284654",
            "name": "height",
            "type": "INT",
            "linkIds": [
              329
            ],
            "pos": [
              -112.86636868943219,
              -605.9977743396407
            ]
          },
          {
            "id": "16c15d42-50c2-44e4-85c8-5726396f6f17",
            "name": "lora_name",
            "type": "COMBO",
            "linkIds": [
              332,
              1312
            ],
            "pos": [
              -112.86636868943219,
              -585.9977743396407
            ]
          },
          {
            "id": "8be1812d-87a4-4a91-8f3e-7b748a24b176",
            "name": "strength_model",
            "type": "FLOAT",
            "linkIds": [
              333,
              1313
            ],
            "pos": [
              -112.86636868943219,
              -565.9977743396407
            ]
          },
          {
            "id": "69dff8a0-c242-4bb2-a130-9d1ddea79bd2",
            "name": "unet_name",
            "type": "COMBO",
            "linkIds": [
              334
            ],
            "pos": [
              -112.86636868943219,
              -545.9977743396407
            ]
          },
          {
            "id": "a20a6289-01aa-4dc5-aeca-be8c347569e9",
            "name": "clip_name",
            "type": "COMBO",
            "linkIds": [
              335
            ],
            "pos": [
              -112.86636868943219,
              -525.9977743396407
            ]
          },
          {
            "id": "5ef38fd5-20e0-4665-955d-0e4873bb8a5d",
            "name": "vae_name",
            "type": "COMBO",
            "linkIds": [
              336
            ],
            "pos": [
              -112.86636868943219,
              -505.9977743396407
            ]
          }
        ],
        "outputs": [
          {
            "id": "4428fbe9-87ff-4269-ab8c-3c99f26fd122",
            "name": "IMAGE",
            "type": "IMAGE",
            "linkIds": [
              85
            ],
            "localized_name": "IMAGE",
            "pos": [
              1760.8874614635452,
              -722.7013262850722
            ]
          }
        ],
        "widgets": [],
        "nodes": [
          {
            "id": 18,
            "type": "CLIPLoader",
            "pos": [
              115.54008939317045,
              -590.6751117414634
            ],
            "size": [
              270,
              120
            ],
            "flags": {},
            "order": 11,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "clip_name",
                "name": "clip_name",
                "type": "COMBO",
                "widget": {
                  "name": "clip_name"
                },
                "link": 335
              }
            ],
            "outputs": [
              {
                "localized_name": "CLIP",
                "name": "CLIP",
                "type": "CLIP",
                "links": [
                  43,
                  44
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.73",
              "Node name for S&R": "CLIPLoader",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "qwen_3_4b.safetensors",
              "lumina2",
              "default"
            ]
          },
          {
            "id": 17,
            "type": "VAELoader",
            "pos": [
              431.69159223157635,
              -555.6088314910745
            ],
            "size": [
              270,
              63.33333333333334
            ],
            "flags": {},
            "order": 10,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "vae_name",
                "name": "vae_name",
                "type": "COMBO",
                "widget": {
                  "name": "vae_name"
                },
                "link": 336
              }
            ],
            "outputs": [
              {
                "localized_name": "VAE",
                "name": "VAE",
                "type": "VAE",
                "links": [
                  45
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.73",
              "Node name for S&R": "VAELoader",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "ae.safetensors"
            ]
          },
          {
            "id": 82,
            "type": "FlowMatchEulerDiscreteScheduler (Custom)",
            "pos": [
              745.5912661843734,
              -325.5869869374754
            ],
            "size": [
              389.9,
              466
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "sigmas",
                "name": "sigmas",
                "type": "SIGMAS",
                "links": [
                  205
                ]
              }
            ],
            "properties": {
              "cnr_id": "erosdiffusion-eulerflowmatchingdiscretescheduler",
              "ver": "1.0.7",
              "Node name for S&R": "FlowMatchEulerDiscreteScheduler (Custom)",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              10,
              0,
              10,
              256,
              0.5,
              "disable",
              8192,
              1.15,
              1000,
              3,
              0,
              "disable",
              "exponential",
              "disable",
              "disable",
              "disable",
              "disable",
              "cuda"
            ]
          },
          {
            "id": 85,
            "type": "KSamplerSelect",
            "pos": [
              1089.4017285543387,
              -717.4033977996079
            ],
            "size": [
              315,
              58
            ],
            "flags": {},
            "order": 1,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "SAMPLER",
                "name": "SAMPLER",
                "type": "SAMPLER",
                "slot_index": 0,
                "links": [
                  207,
                  344
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.43",
              "Node name for S&R": "KSamplerSelect",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "dpmpp_sde"
            ]
          },
          {
            "id": 196,
            "type": "FlowMatchEulerDiscreteScheduler (Custom)",
            "pos": [
              1317.0246792531677,
              -330.99943234556173
            ],
            "size": [
              389.9,
              466
            ],
            "flags": {},
            "order": 2,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "sigmas",
                "name": "sigmas",
                "type": "SIGMAS",
                "links": [
                  346
                ]
              }
            ],
            "properties": {
              "cnr_id": "erosdiffusion-eulerflowmatchingdiscretescheduler",
              "ver": "1.0.7",
              "Node name for S&R": "FlowMatchEulerDiscreteScheduler (Custom)",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              20,
              10,
              20,
              256,
              0.5,
              "disable",
              8192,
              1.15,
              1000,
              3,
              0,
              "disable",
              "exponential",
              "disable",
              "disable",
              "disable",
              "disable",
              "cuda"
            ]
          },
          {
            "id": 6,
            "type": "CLIPTextEncode",
            "pos": [
              204.1387515816354,
              -360.1314201421249
            ],
            "size": [
              450,
              285
            ],
            "flags": {
              "collapsed": true
            },
            "order": 6,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "clip",
                "name": "clip",
                "type": "CLIP",
                "link": 43
              },
              {
                "localized_name": "text",
                "name": "text",
                "type": "STRING",
                "widget": {
                  "name": "text"
                },
                "link": 147
              }
            ],
            "outputs": [
              {
                "localized_name": "CONDITIONING",
                "name": "CONDITIONING",
                "type": "CONDITIONING",
                "slot_index": 0,
                "links": [
                  203,
                  341
                ]
              }
            ],
            "title": "CLIP Text Encode (Positive Prompt)",
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.73",
              "Node name for S&R": "CLIPTextEncode",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "A cinematic HDR headshot photograph of a female fashion model with smooth olive skin, long wavy dark brown hair flowing over her shoulders, and striking green eyes. She wears a sleek black blazer and subtle gold earrings. The mood is elegant and confident. The background is a softly blurred upscale studio with neutral matte tones that enhance her features. Camera angle is eye-level and tightly framed on her face with shallow depth of field. Soft studio lighting highlights her cheekbones. The scene is indoors during the daytime with controlled studio lighting, ultra-sharp focus, professional fashion photography style."
            ],
            "color": "#232",
            "bgcolor": "#353"
          },
          {
            "id": 7,
            "type": "CLIPTextEncode",
            "pos": [
              193.9227158243673,
              -303.50836988716475
            ],
            "size": [
              420,
              135
            ],
            "flags": {
              "collapsed": true
            },
            "order": 7,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "clip",
                "name": "clip",
                "type": "CLIP",
                "link": 44
              },
              {
                "localized_name": "text",
                "name": "text",
                "type": "STRING",
                "widget": {
                  "name": "text"
                },
                "link": 148
              }
            ],
            "outputs": [
              {
                "localized_name": "CONDITIONING",
                "name": "CONDITIONING",
                "type": "CONDITIONING",
                "slot_index": 0,
                "links": [
                  204,
                  342
                ]
              }
            ],
            "title": "CLIP Text Encode (Negative Prompt)",
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.73",
              "Node name for S&R": "CLIPTextEncode",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "bad hands, extra fingers, missing fingers, fused fingers, broken hands, mutant hands, twisted limbs, extra limbs, missing limbs, dimple "
            ],
            "color": "#322",
            "bgcolor": "#533"
          },
          {
            "id": 8,
            "type": "VAEDecode",
            "pos": [
              1451.3030722695903,
              -726.011321579222
            ],
            "size": [
              210,
              55
            ],
            "flags": {},
            "order": 8,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "samples",
                "name": "samples",
                "type": "LATENT",
                "link": 345
              },
              {
                "localized_name": "vae",
                "name": "vae",
                "type": "VAE",
                "link": 45
              }
            ],
            "outputs": [
              {
                "localized_name": "IMAGE",
                "name": "IMAGE",
                "type": "IMAGE",
                "slot_index": 0,
                "links": [
                  85
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.73",
              "Node name for S&R": "VAEDecode",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": []
          },
          {
            "id": 86,
            "type": "SamplerCustom",
            "pos": [
              793.1455042735737,
              -613.940332786725
            ],
            "size": [
              270,
              230
            ],
            "flags": {},
            "order": 12,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "model",
                "name": "model",
                "type": "MODEL",
                "link": 331
              },
              {
                "localized_name": "positive",
                "name": "positive",
                "type": "CONDITIONING",
                "link": 203
              },
              {
                "localized_name": "negative",
                "name": "negative",
                "type": "CONDITIONING",
                "link": 204
              },
              {
                "localized_name": "sampler",
                "name": "sampler",
                "type": "SAMPLER",
                "link": 207
              },
              {
                "localized_name": "sigmas",
                "name": "sigmas",
                "type": "SIGMAS",
                "link": 205
              },
              {
                "localized_name": "latent_image",
                "name": "latent_image",
                "type": "LATENT",
                "link": 327
              },
              {
                "localized_name": "noise_seed",
                "name": "noise_seed",
                "type": "INT",
                "widget": {
                  "name": "noise_seed"
                },
                "link": 219
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "LATENT",
                "links": [
                  338
                ]
              },
              {
                "localized_name": "denoised_output",
                "name": "denoised_output",
                "type": "LATENT",
                "links": null
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.75",
              "Node name for S&R": "SamplerCustom",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              true,
              500,
              "randomize",
              1
            ]
          },
          {
            "id": 193,
            "type": "EmptyLatentImage",
            "pos": [
              795.5155696836863,
              -761.6757429151827
            ],
            "size": [
              270,
              106
            ],
            "flags": {},
            "order": 13,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "width",
                "name": "width",
                "type": "INT",
                "widget": {
                  "name": "width"
                },
                "link": 328
              },
              {
                "localized_name": "height",
                "name": "height",
                "type": "INT",
                "widget": {
                  "name": "height"
                },
                "link": 329
              }
            ],
            "outputs": [
              {
                "localized_name": "LATENT",
                "name": "LATENT",
                "type": "LATENT",
                "links": [
                  327
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.16.3",
              "Node name for S&R": "EmptyLatentImage",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              1280,
              720,
              1
            ]
          },
          {
            "id": 195,
            "type": "SamplerCustom",
            "pos": [
              1423.285705953142,
              -614.0871888924383
            ],
            "size": [
              270,
              230
            ],
            "flags": {},
            "order": 15,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "model",
                "name": "model",
                "type": "MODEL",
                "link": 1315
              },
              {
                "localized_name": "positive",
                "name": "positive",
                "type": "CONDITIONING",
                "link": 341
              },
              {
                "localized_name": "negative",
                "name": "negative",
                "type": "CONDITIONING",
                "link": 342
              },
              {
                "localized_name": "sampler",
                "name": "sampler",
                "type": "SAMPLER",
                "link": 344
              },
              {
                "localized_name": "sigmas",
                "name": "sigmas",
                "type": "SIGMAS",
                "link": 346
              },
              {
                "localized_name": "latent_image",
                "name": "latent_image",
                "type": "LATENT",
                "link": 339
              }
            ],
            "outputs": [
              {
                "localized_name": "output",
                "name": "output",
                "type": "LATENT",
                "links": [
                  345
                ]
              },
              {
                "localized_name": "denoised_output",
                "name": "denoised_output",
                "type": "LATENT",
                "links": null
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.75",
              "Node name for S&R": "SamplerCustom",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              true,
              562642118843572,
              "randomize",
              1
            ]
          },
          {
            "id": 197,
            "type": "LatentUpscale",
            "pos": [
              1106.6042640877206,
              -591.4964422344175
            ],
            "size": [
              270,
              130
            ],
            "flags": {},
            "order": 16,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "samples",
                "name": "samples",
                "type": "LATENT",
                "link": 338
              }
            ],
            "outputs": [
              {
                "localized_name": "LATENT",
                "name": "LATENT",
                "type": "LATENT",
                "links": [
                  339
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.16.3",
              "Node name for S&R": "LatentUpscale",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              "area",
              1920,
              1080,
              "disabled"
            ]
          },
          {
            "id": 819,
            "type": "LoraLoaderModelOnly",
            "pos": [
              281.80803460231357,
              -997.880146781961
            ],
            "size": [
              475.305254525084,
              122.95642565586923
            ],
            "flags": {},
            "order": 17,
            "mode": 4,
            "inputs": [
              {
                "localized_name": "model",
                "name": "model",
                "type": "MODEL",
                "link": 1286
              }
            ],
            "outputs": [
              {
                "localized_name": "MODEL",
                "name": "MODEL",
                "type": "MODEL",
                "links": [
                  1287
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.16.3",
              "Node name for S&R": "LoraLoaderModelOnly",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              "zimage\\ZIT-RAZ'SOPTICLAB-CORE.safetensors",
              0.3
            ]
          },
          {
            "id": 16,
            "type": "UNETLoader",
            "pos": [
              116.9064951295994,
              -752.5894828208529
            ],
            "size": [
              270,
              91.66666666666667
            ],
            "flags": {},
            "order": 9,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "unet_name",
                "name": "unet_name",
                "type": "COMBO",
                "widget": {
                  "name": "unet_name"
                },
                "link": 334
              }
            ],
            "outputs": [
              {
                "localized_name": "MODEL",
                "name": "MODEL",
                "type": "MODEL",
                "links": [
                  1286,
                  1314
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.3.73",
              "Node name for S&R": "UNETLoader",
              "ue_properties": {
                "version": "7.5.2",
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "z_image_turbo_bf16.safetensors",
              "default"
            ]
          },
          {
            "id": 825,
            "type": "MarkdownNote",
            "pos": [
              1264.238968961083,
              -1320.23890245542
            ],
            "size": [
              330.0826446280993,
              111.29075882794882
            ],
            "flags": {},
            "order": 4,
            "mode": 0,
            "inputs": [],
            "outputs": [],
            "properties": {
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "# This blonde character lora can be found [HERE](https://huggingface.co/vrgamedevgirl84/BlondeFemaleZimageLora/blob/main/BlondeFemaleCharacterLora.safetensors)\nOr use your own. "
            ],
            "color": "#432",
            "bgcolor": "#653"
          },
          {
            "id": 834,
            "type": "LoraLoaderModelOnly",
            "pos": [
              1364.7973414199937,
              -1098.4802124778053
            ],
            "size": [
              337.25441796763425,
              121.56142233390244
            ],
            "flags": {},
            "order": 5,
            "mode": 4,
            "inputs": [
              {
                "localized_name": "model",
                "name": "model",
                "type": "MODEL",
                "link": 1314
              },
              {
                "localized_name": "lora_name",
                "name": "lora_name",
                "type": "COMBO",
                "widget": {
                  "name": "lora_name"
                },
                "link": 1312
              },
              {
                "localized_name": "strength_model",
                "name": "strength_model",
                "type": "FLOAT",
                "widget": {
                  "name": "strength_model"
                },
                "link": 1313
              }
            ],
            "outputs": [
              {
                "localized_name": "MODEL",
                "name": "MODEL",
                "type": "MODEL",
                "links": [
                  1315
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.16.3",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              },
              "Node name for S&R": "LoraLoaderModelOnly"
            },
            "widgets_values": [
              "BlondeFemaleCharacterLora.safetensors",
              0.8
            ]
          },
          {
            "id": 194,
            "type": "LoraLoaderModelOnly",
            "pos": [
              981.2197735108144,
              -1098.6538514601516
            ],
            "size": [
              337.25441796763425,
              121.56142233390244
            ],
            "flags": {},
            "order": 14,
            "mode": 4,
            "inputs": [
              {
                "localized_name": "model",
                "name": "model",
                "type": "MODEL",
                "link": 1287
              },
              {
                "localized_name": "lora_name",
                "name": "lora_name",
                "type": "COMBO",
                "widget": {
                  "name": "lora_name"
                },
                "link": 332
              },
              {
                "localized_name": "strength_model",
                "name": "strength_model",
                "type": "FLOAT",
                "widget": {
                  "name": "strength_model"
                },
                "link": 333
              }
            ],
            "outputs": [
              {
                "localized_name": "MODEL",
                "name": "MODEL",
                "type": "MODEL",
                "links": [
                  331
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.16.3",
              "Node name for S&R": "LoraLoaderModelOnly",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              "BlondeFemaleCharacterLora.safetensors",
              0.8
            ]
          },
          {
            "id": 824,
            "type": "MarkdownNote",
            "pos": [
              361.7858115800739,
              -1221.8542640940257
            ],
            "size": [
              304.5379413974455,
              88
            ],
            "flags": {},
            "order": 3,
            "mode": 0,
            "inputs": [],
            "outputs": [],
            "properties": {
              "ue_properties": {
                "widget_ue_connectable": {},
                "version": "7.5.2",
                "input_ue_unconnectable": {}
              }
            },
            "widgets_values": [
              "# This lora can be found [HERE](https://civitai.com/models/2546000/razs-optic-lab-photography-style-zit)"
            ],
            "color": "#432",
            "bgcolor": "#653"
          }
        ],
        "groups": [
          {
            "id": 8,
            "title": "Group",
            "bounding": [
              735.5912661843734,
              -835.2757429151827,
              1101.7865181833015,
              1022.5534554218699
            ],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
          },
          {
            "id": 10,
            "title": "Group",
            "bounding": [
              105.54008939317045,
              -826.189482820853,
              608.9878492831501,
              532.6811129336879
            ],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
          },
          {
            "id": 28,
            "title": "Group",
            "bounding": [
              880.9099385279075,
              -1393.8389024554199,
              846.3748050737048,
              543.3436345183973
            ],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
          },
          {
            "id": 29,
            "title": "Group",
            "bounding": [
              271.80803460231357,
              -1343.3293573379763,
              495.305254525084,
              478.4056362118846
            ],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
          }
        ],
        "links": [
          {
            "id": 44,
            "origin_id": 18,
            "origin_slot": 0,
            "target_id": 7,
            "target_slot": 0,
            "type": "CLIP"
          },
          {
            "id": 45,
            "origin_id": 17,
            "origin_slot": 0,
            "target_id": 8,
            "target_slot": 1,
            "type": "VAE"
          },
          {
            "id": 43,
            "origin_id": 18,
            "origin_slot": 0,
            "target_id": 6,
            "target_slot": 0,
            "type": "CLIP"
          },
          {
            "id": 85,
            "origin_id": 8,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 0,
            "type": "IMAGE"
          },
          {
            "id": 147,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 6,
            "target_slot": 1,
            "type": "STRING"
          },
          {
            "id": 148,
            "origin_id": -10,
            "origin_slot": 1,
            "target_id": 7,
            "target_slot": 1,
            "type": "STRING"
          },
          {
            "id": 203,
            "origin_id": 6,
            "origin_slot": 0,
            "target_id": 86,
            "target_slot": 1,
            "type": "CONDITIONING"
          },
          {
            "id": 204,
            "origin_id": 7,
            "origin_slot": 0,
            "target_id": 86,
            "target_slot": 2,
            "type": "CONDITIONING"
          },
          {
            "id": 205,
            "origin_id": 82,
            "origin_slot": 0,
            "target_id": 86,
            "target_slot": 4,
            "type": "SIGMAS"
          },
          {
            "id": 207,
            "origin_id": 85,
            "origin_slot": 0,
            "target_id": 86,
            "target_slot": 3,
            "type": "SAMPLER"
          },
          {
            "id": 219,
            "origin_id": -10,
            "origin_slot": 2,
            "target_id": 86,
            "target_slot": 6,
            "type": "INT"
          },
          {
            "id": 327,
            "origin_id": 193,
            "origin_slot": 0,
            "target_id": 86,
            "target_slot": 5,
            "type": "LATENT"
          },
          {
            "id": 328,
            "origin_id": -10,
            "origin_slot": 3,
            "target_id": 193,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 329,
            "origin_id": -10,
            "origin_slot": 4,
            "target_id": 193,
            "target_slot": 1,
            "type": "INT"
          },
          {
            "id": 331,
            "origin_id": 194,
            "origin_slot": 0,
            "target_id": 86,
            "target_slot": 0,
            "type": "MODEL"
          },
          {
            "id": 332,
            "origin_id": -10,
            "origin_slot": 5,
            "target_id": 194,
            "target_slot": 1,
            "type": "COMBO"
          },
          {
            "id": 333,
            "origin_id": -10,
            "origin_slot": 6,
            "target_id": 194,
            "target_slot": 2,
            "type": "FLOAT"
          },
          {
            "id": 334,
            "origin_id": -10,
            "origin_slot": 7,
            "target_id": 16,
            "target_slot": 0,
            "type": "COMBO"
          },
          {
            "id": 335,
            "origin_id": -10,
            "origin_slot": 8,
            "target_id": 18,
            "target_slot": 0,
            "type": "COMBO"
          },
          {
            "id": 336,
            "origin_id": -10,
            "origin_slot": 9,
            "target_id": 17,
            "target_slot": 0,
            "type": "COMBO"
          },
          {
            "id": 338,
            "origin_id": 86,
            "origin_slot": 0,
            "target_id": 197,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 339,
            "origin_id": 197,
            "origin_slot": 0,
            "target_id": 195,
            "target_slot": 5,
            "type": "LATENT"
          },
          {
            "id": 341,
            "origin_id": 6,
            "origin_slot": 0,
            "target_id": 195,
            "target_slot": 1,
            "type": "CONDITIONING"
          },
          {
            "id": 342,
            "origin_id": 7,
            "origin_slot": 0,
            "target_id": 195,
            "target_slot": 2,
            "type": "CONDITIONING"
          },
          {
            "id": 344,
            "origin_id": 85,
            "origin_slot": 0,
            "target_id": 195,
            "target_slot": 3,
            "type": "SAMPLER"
          },
          {
            "id": 345,
            "origin_id": 195,
            "origin_slot": 0,
            "target_id": 8,
            "target_slot": 0,
            "type": "LATENT"
          },
          {
            "id": 346,
            "origin_id": 196,
            "origin_slot": 0,
            "target_id": 195,
            "target_slot": 4,
            "type": "SIGMAS"
          },
          {
            "id": 1286,
            "origin_id": 16,
            "origin_slot": 0,
            "target_id": 819,
            "target_slot": 0,
            "type": "MODEL"
          },
          {
            "id": 1287,
            "origin_id": 819,
            "origin_slot": 0,
            "target_id": 194,
            "target_slot": 0,
            "type": "MODEL"
          },
          {
            "id": 1312,
            "origin_id": -10,
            "origin_slot": 5,
            "target_id": 834,
            "target_slot": 1,
            "type": "COMBO"
          },
          {
            "id": 1313,
            "origin_id": -10,
            "origin_slot": 6,
            "target_id": 834,
            "target_slot": 2,
            "type": "FLOAT"
          },
          {
            "id": 1314,
            "origin_id": 16,
            "origin_slot": 0,
            "target_id": 834,
            "target_slot": 0,
            "type": "MODEL"
          },
          {
            "id": 1315,
            "origin_id": 834,
            "origin_slot": 0,
            "target_id": 195,
            "target_slot": 0,
            "type": "MODEL"
          }
        ],
        "extra": {
          "workflowRendererVersion": "LG",
          "ue_links": [],
          "links_added_by_ue": []
        }
      },
      {
        "id": "dd449f08-b59d-45b5-b1de-1a23ab740fc1",
        "version": 1,
        "state": {
          "lastGroupId": 29,
          "lastNodeId": 834,
          "lastLinkId": 1315,
          "lastRerouteId": 0
        },
        "revision": 0,
        "config": {},
        "name": "New Subgraph",
        "inputNode": {
          "id": -10,
          "bounding": [
            -1695.9018288331026,
            5617.863489173302,
            146,
            180
          ]
        },
        "outputNode": {
          "id": -20,
          "bounding": [
            -229.31592661639678,
            5735.7915463779655,
            120,
            60
          ]
        },
        "inputs": [
          {
            "id": "f3fb2d4f-c9ba-4b30-a016-021b4c689725",
            "name": "index",
            "type": "INT",
            "linkIds": [
              1296
            ],
            "localized_name": "index",
            "pos": [
              -1569.9018288331026,
              5637.863489173302
            ]
          },
          {
            "id": "a8882da8-dc57-4cca-8475-572c62423c97",
            "name": "string_1",
            "type": "STRING",
            "linkIds": [
              1304
            ],
            "pos": [
              -1569.9018288331026,
              5657.863489173302
            ]
          },
          {
            "id": "6e0553a0-ad2c-49f7-9bc2-f11e654696d2",
            "name": "items",
            "type": "STRING",
            "linkIds": [
              1305
            ],
            "pos": [
              -1569.9018288331026,
              5677.863489173302
            ]
          },
          {
            "id": "cbbd9d79-c05b-469d-9ca0-6057d9943578",
            "name": "label",
            "type": "STRING",
            "linkIds": [
              1306
            ],
            "pos": [
              -1569.9018288331026,
              5697.863489173302
            ]
          },
          {
            "id": "4686a0b0-5872-4629-a17a-73fd7fd00544",
            "name": "pick_count",
            "type": "INT",
            "linkIds": [
              1307
            ],
            "pos": [
              -1569.9018288331026,
              5717.863489173302
            ]
          },
          {
            "id": "8885c95f-29a9-4cbc-a5e2-afe2ea33e279",
            "name": "selection_mode",
            "type": "COMBO",
            "linkIds": [
              1308
            ],
            "pos": [
              -1569.9018288331026,
              5737.863489173302
            ]
          },
          {
            "id": "1a32190b-af94-4d6c-8d7f-46d4de34973c",
            "name": "two_item_template",
            "type": "STRING",
            "linkIds": [
              1309
            ],
            "pos": [
              -1569.9018288331026,
              5757.863489173302
            ]
          }
        ],
        "outputs": [
          {
            "id": "6fbb5b33-aa6a-4e65-909e-b54995114771",
            "name": "text",
            "type": "STRING",
            "linkIds": [
              1298,
              1299
            ],
            "localized_name": "text",
            "pos": [
              -209.31592661639678,
              5755.7915463779655
            ]
          }
        ],
        "widgets": [],
        "nodes": [
          {
            "id": 828,
            "type": "PrimitiveInt",
            "pos": [
              -1202.5265719256067,
              5920.776377653596
            ],
            "size": [
              270,
              82
            ],
            "flags": {},
            "order": 0,
            "mode": 0,
            "inputs": [],
            "outputs": [
              {
                "localized_name": "INT",
                "name": "INT",
                "type": "INT",
                "links": [
                  1300
                ]
              }
            ],
            "properties": {
              "cnr_id": "comfy-core",
              "ver": "0.16.2",
              "Node name for S&R": "PrimitiveInt",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              -926216702286978,
              "randomize"
            ]
          },
          {
            "id": 826,
            "type": "VRGDG_MultiStringConcat",
            "pos": [
              -751.6817260996323,
              5443.862960929588
            ],
            "size": [
              400,
              244
            ],
            "flags": {},
            "order": 2,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "string_1",
                "name": "string_1",
                "type": "STRING",
                "widget": {
                  "name": "string_1"
                },
                "link": 1304
              },
              {
                "localized_name": "string_2",
                "name": "string_2",
                "type": "STRING",
                "widget": {
                  "name": "string_2"
                },
                "link": 1297
              }
            ],
            "outputs": [
              {
                "localized_name": "text",
                "name": "text",
                "type": "STRING",
                "links": [
                  1298,
                  1299
                ]
              }
            ],
            "properties": {
              "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
              "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
              "Node name for S&R": "VRGDG_MultiStringConcat",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              3,
              "\\n\\n",
              "Convert the user’s text-to-image prompt into a dynamic image-to-video prompt.\n\nUse the image prompt only as the visual reference. Preserve the original subject, setting, outfit, mood, atmosphere, and scene identity. Do not repeat or describe color grading, lighting style, camera photo style, or static image-quality terms unless needed for motion clarity.\n\nAdd fast, cinematic motion by giving the subject a clear action sequence, expressive face expressions and body movement, strong gestures, and intentional camera movement. Keep the subject visible and framed throughout.\n\nOutput one polished paragraph using this structure:\n\nThe [Subject] who is singing with passion in [setting/environment] during [time/weather]. The subject [dynamic performance action]. Their clothing/hair [reacts to movement]. The camera [Camera Motion] while maintaining [subject visibility]. The environment [reacts dynamically].\n\neach word in brackets should be chosen based of user input that would best fit the scene.\nNOTE: DO NOT USE ORBIT TYPE CAMERA MOTION, DO NOT USE THE WORD \"SPIN\" SUBJECT SHOULD NEVER SPIN \nSubject should always be physically singing!\n\nDo not add audio, dialogue, captions, text overlays, unrelated characters, new locations, major story changes, color style, lighting style, or image-quality descriptions. Keep it vivid, fast, cinematic, dynamic, and video-ready.\n",
              "",
              "\nText-to-image prompt to convert:\n",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              ""
            ]
          },
          {
            "id": 825,
            "type": "VRGDG_CyclingTextPicker",
            "pos": [
              -1207.3596872632995,
              5446.863489173302
            ],
            "size": [
              431.7216733663855,
              432
            ],
            "flags": {},
            "order": 1,
            "mode": 0,
            "inputs": [
              {
                "localized_name": "index",
                "name": "index",
                "type": "INT",
                "widget": {
                  "name": "index"
                },
                "link": 1296
              },
              {
                "localized_name": "items",
                "name": "items",
                "type": "STRING",
                "widget": {
                  "name": "items"
                },
                "link": 1305
              },
              {
                "localized_name": "label",
                "name": "label",
                "type": "STRING",
                "widget": {
                  "name": "label"
                },
                "link": 1306
              },
              {
                "localized_name": "pick_count",
                "name": "pick_count",
                "type": "INT",
                "widget": {
                  "name": "pick_count"
                },
                "link": 1307
              },
              {
                "localized_name": "selection_mode",
                "name": "selection_mode",
                "type": "COMBO",
                "widget": {
                  "name": "selection_mode"
                },
                "link": 1308
              },
              {
                "localized_name": "seed",
                "name": "seed",
                "type": "INT",
                "widget": {
                  "name": "seed"
                },
                "link": 1300
              },
              {
                "localized_name": "two_item_template",
                "name": "two_item_template",
                "type": "STRING",
                "widget": {
                  "name": "two_item_template"
                },
                "link": 1309
              }
            ],
            "outputs": [
              {
                "localized_name": "formatted_text",
                "name": "formatted_text",
                "type": "STRING",
                "links": [
                  1297
                ]
              },
              {
                "localized_name": "selected_item",
                "name": "selected_item",
                "type": "STRING",
                "links": null
              },
              {
                "localized_name": "selected_items",
                "name": "selected_items",
                "type": "STRING",
                "links": null
              },
              {
                "localized_name": "wrapped_index",
                "name": "wrapped_index",
                "type": "INT",
                "links": null
              },
              {
                "localized_name": "item_count",
                "name": "item_count",
                "type": "INT",
                "links": null
              }
            ],
            "properties": {
              "aux_id": "vrgamegirl19/comfyui-vrgamedevgirl",
              "ver": "030410c766ca6f8ef417a352b1311a84da2670f6",
              "Node name for S&R": "VRGDG_CyclingTextPicker",
              "ue_properties": {
                "widget_ue_connectable": {},
                "input_ue_unconnectable": {},
                "version": "7.5.2"
              }
            },
            "widgets_values": [
              0,
              "slow push in\nslow pull out\ndolly in\ndolly out\ntruck left\ntruck right\npan left\npan right\ntilt up\ntilt down\ncrane up\ncrane down\norbit left\norbit right\nhandheld follow\nwhip pan\nrack focus\nlow angle tracking shot\noverhead descending shot\nsteadicam walk forward\n",
              "Camera Motion",
              0,
              2,
              "auto",
              "index",
              196120625027564,
              "randomize",
              "auto",
              "begin with {item1}, then transition into {item2}",
              false
            ]
          }
        ],
        "groups": [],
        "links": [
          {
            "id": 1300,
            "origin_id": 828,
            "origin_slot": 0,
            "target_id": 825,
            "target_slot": 5,
            "type": "INT"
          },
          {
            "id": 1297,
            "origin_id": 825,
            "origin_slot": 0,
            "target_id": 826,
            "target_slot": 1,
            "type": "STRING"
          },
          {
            "id": 1296,
            "origin_id": -10,
            "origin_slot": 0,
            "target_id": 825,
            "target_slot": 0,
            "type": "INT"
          },
          {
            "id": 1298,
            "origin_id": 826,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 0,
            "type": "STRING"
          },
          {
            "id": 1299,
            "origin_id": 826,
            "origin_slot": 0,
            "target_id": -20,
            "target_slot": 0,
            "type": "STRING"
          },
          {
            "id": 1304,
            "origin_id": -10,
            "origin_slot": 1,
            "target_id": 826,
            "target_slot": 0,
            "type": "STRING"
          },
          {
            "id": 1305,
            "origin_id": -10,
            "origin_slot": 2,
            "target_id": 825,
            "target_slot": 1,
            "type": "STRING"
          },
          {
            "id": 1306,
            "origin_id": -10,
            "origin_slot": 3,
            "target_id": 825,
            "target_slot": 2,
            "type": "STRING"
          },
          {
            "id": 1307,
            "origin_id": -10,
            "origin_slot": 4,
            "target_id": 825,
            "target_slot": 3,
            "type": "INT"
          },
          {
            "id": 1308,
            "origin_id": -10,
            "origin_slot": 5,
            "target_id": 825,
            "target_slot": 4,
            "type": "COMBO"
          },
          {
            "id": 1309,
            "origin_id": -10,
            "origin_slot": 6,
            "target_id": 825,
            "target_slot": 6,
            "type": "STRING"
          }
        ],
        "extra": {
          "workflowRendererVersion": "LG",
          "ue_links": []
        }
      }
    ]
  },
  "config": {},
  "extra": {
    "frontendVersion": "1.39.19",
    "workflowRendererVersion": "LG",
    "prompt": {
      "1": {
        "inputs": {
          "ckpt_name": "ltx-av-step-1751000_vocoder_24K.safetensors"
        },
        "class_type": "CheckpointLoaderSimple",
        "_meta": {
          "title": "Load Checkpoint"
        }
      },
      "2": {
        "inputs": {
          "gemma_path": "gemma-3-12b-it-qat-q4_0-unquantized_readout_proj/model/model.safetensors",
          "ltxv_path": "ltx-av-step-1751000_vocoder_24K.safetensors",
          "max_length": 1024
        },
        "class_type": "LTXVGemmaCLIPModelLoader",
        "_meta": {
          "title": "🅛🅣🅧 Gemma 3 Model Loader"
        }
      },
      "3": {
        "inputs": {
          "text": "A medium close-up shot features a Caucasian man with a closely shaven head and face, wearing a black baseball cap with \"PNTR\" in white letters on the front, and a dark grey t-shirt with \"JUST DO IT\" visible across his chest. A small black microphone is clipped to his shirt collar. He is positioned slightly to the left of the frame, looking intently downwards and to his right, his eyes focused off-camera. His facial expression is one of deep concentration, with his brow slightly furrowed. As he looks down, a quick sniff sound is heard, and then he speaks with a deep male voice and a slightly frustrated tone, saying, \"I think it's so bad.\" The camera remains static throughout, maintaining a shallow depth of field, which keeps the man in sharp focus while the background is softly blurred, revealing a light-colored wall with white wooden shelving or trim, and a partially open white wooden door on the right. After a brief pause, another short, audible sniff is heard. The man then continues to speak, his voice maintaining the same quality, as he states, \"So bad. So bad.\" He elaborates further, emphasizing his point with a final statement, \"This got to be, it's got to be the worst tool I've ever seen.\"",
          "clip": [
            "2",
            0
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "4": {
        "inputs": {
          "text": "blurry, low quality, still frame, frames, watermark, overlay, titles, has blurbox, has subtitles",
          "clip": [
            "2",
            0
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "8": {
        "inputs": {
          "sampler_name": "euler"
        },
        "class_type": "KSamplerSelect",
        "_meta": {
          "title": "KSamplerSelect"
        }
      },
      "9": {
        "inputs": {
          "steps": 20,
          "max_shift": 2.05,
          "base_shift": 0.95,
          "stretch": true,
          "terminal": 0.1,
          "latent": [
            "28",
            0
          ]
        },
        "class_type": "LTXVScheduler",
        "_meta": {
          "title": "LTXVScheduler"
        }
      },
      "11": {
        "inputs": {
          "noise_seed": 10
        },
        "class_type": "RandomNoise",
        "_meta": {
          "title": "RandomNoise"
        }
      },
      "12": {
        "inputs": {
          "samples": [
            "29",
            0
          ],
          "vae": [
            "1",
            2
          ]
        },
        "class_type": "VAEDecode",
        "_meta": {
          "title": "VAE Decode"
        }
      },
      "13": {
        "inputs": {
          "ckpt_name": "ltx-av-step-1751000_vocoder_24K.safetensors"
        },
        "class_type": "LTXVAudioVAELoader",
        "_meta": {
          "title": "🅛🅣🅧 LTXV Audio VAE Loader"
        }
      },
      "14": {
        "inputs": {
          "samples": [
            "29",
            1
          ],
          "audio_vae": [
            "13",
            0
          ]
        },
        "class_type": "LTXVAudioVAEDecode",
        "_meta": {
          "title": "🅛🅣🅧 LTXV Audio VAE Decode"
        }
      },
      "15": {
        "inputs": {
          "frame_rate": [
            "23",
            0
          ],
          "loop_count": 0,
          "filename_prefix": "AnimateDiff",
          "format": "video/h264-mp4",
          "pix_fmt": "yuv420p",
          "crf": 19,
          "save_metadata": true,
          "trim_to_audio": false,
          "pingpong": false,
          "save_output": true,
          "images": [
            "12",
            0
          ],
          "audio": [
            "14",
            0
          ]
        },
        "class_type": "VHS_VideoCombine",
        "_meta": {
          "title": "Video Combine 🎥🅥🅗🅢"
        }
      },
      "17": {
        "inputs": {
          "skip_blocks": "29",
          "model": [
            "28",
            1
          ],
          "positive": [
            "22",
            0
          ],
          "negative": [
            "22",
            1
          ],
          "parameters": [
            "18",
            0
          ]
        },
        "class_type": "MultimodalGuider",
        "_meta": {
          "title": "🅛🅣🅧 Multimodal Guider"
        }
      },
      "18": {
        "inputs": {
          "modality": "VIDEO",
          "cfg": 3,
          "stg": 0,
          "rescale": 0,
          "modality_scale": 3,
          "parameters": [
            "19",
            0
          ]
        },
        "class_type": "GuiderParameters",
        "_meta": {
          "title": "🅛🅣🅧 Guider Parameters"
        }
      },
      "19": {
        "inputs": {
          "modality": "AUDIO",
          "cfg": 7,
          "stg": 0,
          "rescale": 0,
          "modality_scale": 3
        },
        "class_type": "GuiderParameters",
        "_meta": {
          "title": "🅛🅣🅧 Guider Parameters"
        }
      },
      "21": {
        "inputs": {
          "audioUI": "",
          "audio": [
            "14",
            0
          ]
        },
        "class_type": "PreviewAudio",
        "_meta": {
          "title": "PreviewAudio"
        }
      },
      "22": {
        "inputs": {
          "frame_rate": [
            "23",
            0
          ],
          "positive": [
            "3",
            0
          ],
          "negative": [
            "4",
            0
          ]
        },
        "class_type": "LTXVConditioning",
        "_meta": {
          "title": "LTXVConditioning"
        }
      },
      "23": {
        "inputs": {
          "value": 25
        },
        "class_type": "FloatConstant",
        "_meta": {
          "title": "Float Constant"
        }
      },
      "26": {
        "inputs": {
          "frames_number": [
            "27",
            0
          ],
          "frame_rate": [
            "42",
            0
          ],
          "batch_size": 1
        },
        "class_type": "LTXVEmptyLatentAudio",
        "_meta": {
          "title": "🅛🅣🅧 LTXV Empty Latent Audio"
        }
      },
      "27": {
        "inputs": {
          "value": 105
        },
        "class_type": "INTConstant",
        "_meta": {
          "title": "INT Constant"
        }
      },
      "28": {
        "inputs": {
          "video_latent": [
            "43",
            0
          ],
          "audio_latent": [
            "26",
            0
          ],
          "model": [
            "44",
            0
          ]
        },
        "class_type": "LTXVConcatAVLatent",
        "_meta": {
          "title": "🅛🅣🅧 LTXV Concat AV Latent"
        }
      },
      "29": {
        "inputs": {
          "av_latent": [
            "41",
            0
          ],
          "model": [
            "28",
            1
          ]
        },
        "class_type": "LTXVSeparateAVLatent",
        "_meta": {
          "title": "🅛🅣🅧 LTXV Separate AV Latent"
        }
      },
      "41": {
        "inputs": {
          "noise": [
            "11",
            0
          ],
          "guider": [
            "17",
            0
          ],
          "sampler": [
            "8",
            0
          ],
          "sigmas": [
            "9",
            0
          ],
          "latent_image": [
            "28",
            0
          ]
        },
        "class_type": "SamplerCustomAdvanced",
        "_meta": {
          "title": "SamplerCustomAdvanced"
        }
      },
      "42": {
        "inputs": {
          "a": [
            "23",
            0
          ]
        },
        "class_type": "CM_FloatToInt",
        "_meta": {
          "title": "FloatToInt"
        }
      },
      "43": {
        "inputs": {
          "width": 768,
          "height": 512,
          "length": [
            "27",
            0
          ],
          "batch_size": 1
        },
        "class_type": "EmptyLTXVLatentVideo",
        "_meta": {
          "title": "EmptyLTXVLatentVideo"
        }
      },
      "44": {
        "inputs": {
          "torch_compile": true,
          "disable_backup": false,
          "model": [
            "1",
            0
          ]
        },
        "class_type": "LTXVSequenceParallelMultiGPUPatcher",
        "_meta": {
          "title": "LTXVSequenceParallelMultiGPUPatcher"
        }
      },
      "45": {
        "inputs": {
          "frame_idx": 0,
          "strength": 1
        },
        "class_type": "LTXVAddGuide",
        "_meta": {
          "title": "LTXVAddGuide"
        }
      }
    },
    "comfy_fork_version": "feature/av_inference@a6994ed1",
    "VHS_latentpreview": true,
    "VHS_latentpreviewrate": 0,
    "VHS_MetadataImage": false,
    "VHS_KeepIntermediate": false,
    "ue_links": [],
    "links_added_by_ue": [],
    "ds": {
      "scale": 0.6653988133167464,
      "offset": [
        761.4058095120013,
        -4913.440364267736
      ]
    }
  },
  "version": 0.4
}
