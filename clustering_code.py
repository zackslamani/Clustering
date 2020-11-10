def load():
    data_files = ['/Users/slamani/Desktop/python test/Brisbane_CityBike.json']
    data = []
    for file in data_files:
        with open(file, 'r') as f:
            for line in f.readlines():
                data.append(json.loads(line))
    data = data[0]
    populate_data_df(data)

def populate_data_df(datastationbike):
    #prepare the data
    df = pd.DataFrame()
    df['latitude'] = list(map(lambda data: data["latitude"], datastationbike))
    df['longitude'] = list(map(lambda data: data["longitude"], datastationbike))
  
  #create clusters
    clustering = KMeans(n_clusters = 4)
    output = clustering.fit_predict(df)
    #vizsualize the data
    color1 = np.array(['red', 'green', 'blue', 'black'])
    plt.scatter(df['latitude'], df['longitude'], c=color1[clustering.labels_])
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    
    print(clustering.cluster_centers_)
    print (output)
