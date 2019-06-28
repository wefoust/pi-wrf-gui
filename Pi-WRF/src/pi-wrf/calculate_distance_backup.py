from math import sin,cos,sqrt,atan2,radians,degrees
import geopy.distance
def calculate_distances(lon1_input,lon2_input,lat1_input,lat2_input):
    R=6373
    lat1=radians(lat1_input)
    lon1=radians(lon1_input)
    lat2=radians(lat2_input)
    lon2=radians(lon2_input)
            
    distance_lon=abs(lon2-lon1)
    distance_lat=abs(lat2-lat1)
    a=sin(distance_lat/2)**2+cos(lat1)*cos(lat2)*sin(distance_lon/2)**2
    c=2*atan2(sqrt(a),sqrt(1-a))
    distance=R*c

    return distance
    

   
    """
    coordinate_1=(lat1_input,lon1_input)
    coordinate_2=(lon2_input,lon2_input)
    distance=geopy.distance.VincentyDistance(coordinate_1,coordinate_2).km
    print(distance)
    return distance
    """
    
#if __name__=='__main':
#    calculate_distances(lon1_input,lon2_input,lat1_input,lat2_input)
