import gpxpy
filename = "./routemaps2.txt"
with open(filename) as file:
    data = file.read()
    latlist = []
    longlist = []
    #----------------- Lat
    end = False
    idx1 = 0
    idx2 = 0
    while end == False:
        idx1 = data.find("lat:", idx1+1)
        idx2 = data.find(",lng:", idx2+1)
        if idx1 == -1:
            end = True
        else:
            print(data[idx1+4:idx2])
            latlist.append(data[idx1+4:idx2])
    #---------------------------------------       
    
    #------------ Lon
    end = False
    idx1 = 0
    idx2 = 0
    while end == False:
        idx1 = data.find("lng:", idx1+1)
        idx2 = data.find("}", idx2+1)
        if idx1 == -1:
            end = True
        else:
            print(data[idx1+4:idx2])
            longlist.append(data[idx1+4:idx2])
    #------------------------------------------
            
if(len(latlist) != len(longlist)):
    print("Error!")
    raise Exception
        
# --------------------

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Create points:
for i in range(len(latlist)):
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(latlist[i], longlist[i]))
#gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1235, 5.1235))
#gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1236, 5.1236))

# You can add routes and waypoints, too...

output = gpx.to_xml()
filename = filename.strip(".txt")
with open("."+filename+".gpx", "w") as text_file:
    text_file.write(output)