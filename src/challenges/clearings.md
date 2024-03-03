# __clearings__

## introduction  

This problem is based on work that I did for the Town of [Cornwall's Conservation Commission in Vermont][ccc] as part of an effort to create [an atlas of wildlife habitat connectivity][ccc-atlas].  

I wanted to make a map that showed locations that were in some stage of recovery from human disturbance; locations where successional processes were playing a role in the structure and composition of land cover, as opposed to places where human activity was the dominant influence on structure and composition.  

I also wanted to avoid both the weeds and the baggage of human vs. nature thinking. So I did not care so much if people cut down trees or sugared or extracted resources from land as long as these activities did not interrupt successional processes from playing a role in the structure and composition of land cover over an extended interval of time.     

One approach to this problem is to bring together maps of undisturbed lands, like tree canopy, wetlands, surface waters. In other words, this approach aims to map the _positive values of space_. [Vermont Conservation Design][vcd] is a good example of this approach. This project mapped habitat blocks by first identifying positive values of space and then subtracting small parts from them (for example, removing zones influenced by roads within blocks). 

For the Cornwall project, I tried a different approach. I first mapped the _negative values of space_ for forest wildlife habitat and then took the inverse to map the positive space for forest wildlife habitat. I thought this reflected the ecological history of Vermont when white immigrants and their industries cleared the indigenous forest in the process of settling the land. So I mapped things that _cleared_ underlying land cover and then took the inverse of this to map _recovering_ lands.     

I found this approach to require a simpler model (with fewer steps) than the alternative approach. 

## challenge  

Make a binary map of clearings for a study region, where clearings use these inputs:  

---  

<center>

| NAME                      | DATA                      | 
| :---                      | :---                      |  
| Agricultural lands        | data.lc.ag                |
| e911 Footprints           | data.e911.footprints      | 
| Building Roofprints       | data.lc.buildings         |
| Land cover                | data.lc.base              |
| Roads                     | data.lc.roads             |  
| Railroads                 | data.lc.rr                |  

</center>  

---  

Clearings should identify locations that meet one or more of these 10 conditions:  

---  

<center>

| CONDITION | DESCRIPTION                                                                                           |  
| :---:     | :---                                                                                                  |
| 1         | Buildings, roads, other pavement, and railroad land cover classes are all clearings.                  |
| 2         | Farm/Vineyard clear all other land cover classes.                                                     |
| 3         | Quarry/Mine clear all other land covers.                                                              | 
| 4         | Stadium/Arena clear all other land cover.                                                             |
| 5         | All Alpine glades or trails (both Expert and Easiest) clear all other land cover.                     |
| 6         | Airports clear all other land cover.                                                                  |
| 7         | Buildings have a zone of influence that clears all other land cover within 100 feet.                  |
| 8         | All railroads and roads (except Class 4 roads) clear all other land cover within 50 feet.             |  
| 9         | Ag clears all other land cover except tree canopy and lands within 20 ft of trees.                    | 
| 10        | Golf courses clear all land cover except tree canopy and lands within 20 ft of trees.                 |



</center>

---  

Although you could run this analysis for the entire state of Vermont, it is good practice to develop and test a model for a smaller region so that you do not have to wait as long for processes to complete while you write and test your code. For a test region, please select Addison from the county collection (data.gov.county). Use the test region to filter all the feature collections used in your solution.  

If your model still runs slowly, you can use a smaller test site (for example, one town in Vermont). Ideally, you want your test site to be small but still representative of the larger study region. For example, in our case, an ideal test site would have both farms/vineyards and ski pistes.   

Please note that this problem will require you to select features by attribute for some layers. For example, you will need to isolate farms/vineyards from the e911 footprint layer. To do this, you may find it helpful to look at the "Entity and Attribute Information" in the layer's metadata. You can find links to metadata in the data repo for e911 footprints and roads. 

## starter  

```js
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  CHALLENGE PROBLEM
//  Clearings in Middlebury, Vermont. 

//  Last modified: insert date
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

var data = require('users/jhowarth/public:modules/data.js');       
print('DATA', data);

var t = require('users/jhowarth/public:modules/tasks.js');
```

## deliverable  

Write a script that produces a single binary image that satisfies the ten conditions described above.  

Please take care to organize your script into meaningful chunks and comment your work. I recommend that you use the header template shown below to keep signify the chunks of your code that satisfies each condition.

```js
// -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
//  CONDITION #
// -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
```

No pressure. Give it your best shot. Let me know if you have questions.  

We will go over a solution next week with cards.  






---

[ccc]: https://cornwallvt.com/cornwall-conservation-commission/
[ccc-atlas]: https://jhowarth.users.earthengine.app/view/cornwall-connectivity
[vcd]: https://anr.vermont.gov/node/1182