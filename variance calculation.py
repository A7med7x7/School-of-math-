def variance(data):
   num=len(data)
   print(data)
   mean = sum(data) /num
   print(mean)
   deviations = [((x - mean)**2)/(num-1) for x in data]
   print(deviations)
   (deviationss) = sum(deviations)

   variance = deviationss*10 /num

   return variance
final = variance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])
print(final)