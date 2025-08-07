import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, BarChart, Bar } from 'recharts';
import { MapPin, Clock, Cloud, TrendingUp, Navigation, AlertTriangle, Car, Route } from 'lucide-react';

const TrafficPredictor = () => {
  const [activeTab, setActiveTab] = useState('predict');
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    startLocation: '',
    endLocation: '',
    departureTime: '',
    weatherCondition: 'clear'
  });

  // Mock historical data
  const historicalData = [
    { time: '06:00', volume: 120, speed: 45, congestion: 'Low' },
    { time: '07:00', volume: 280, speed: 35, congestion: 'Medium' },
    { time: '08:00', volume: 420, speed: 25, congestion: 'High' },
    { time: '09:00', volume: 380, speed: 30, congestion: 'High' },
    { time: '10:00', volume: 250, speed: 40, congestion: 'Medium' },
    { time: '11:00', volume: 200, speed: 45, congestion: 'Low' },
    { time: '12:00', volume: 220, speed: 42, congestion: 'Medium' },
    { time: '13:00', volume: 240, speed: 38, congestion: 'Medium' },
    { time: '14:00', volume: 260, speed: 36, congestion: 'Medium' },
    { time: '15:00', volume: 320, speed: 32, congestion: 'High' },
    { time: '16:00', volume: 380, speed: 28, congestion: 'High' },
    { time: '17:00', volume: 450, speed: 22, congestion: 'High' },
    { time: '18:00', volume: 480, speed: 20, congestion: 'High' },
    { time: '19:00', volume: 350, speed: 30, congestion: 'High' },
    { time: '20:00', volume: 280, speed: 35, congestion: 'Medium' },
    { time: '21:00', volume: 200, speed: 42, congestion: 'Low' }
  ];

  const routeData = [
    { route: 'Route A (Highway)', distance: '15.2 km', time: '22 min', traffic: 'Medium', fuel: '1.2L' },
    { route: 'Route B (City Roads)', distance: '12.8 km', time: '28 min', traffic: 'High', fuel: '1.4L' },
    { route: 'Route C (Mixed)', distance: '14.1 km', time: '25 min', traffic: 'Low', fuel: '1.1L' }
  ];

  const currentStats = {
    averageSpeed: 32,
    congestionLevel: 75,
    activeVehicles: 15420,
    weatherImpact: 15
  };

  // Mock prediction function
  const generatePrediction = async () => {
    setLoading(true);
    
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    const hour = new Date(formData.departureTime).getHours();
    const baseTraffic = historicalData.find(d => parseInt(d.time.split(':')[0]) === hour) || historicalData[8];
    
    const weatherMultiplier = {
      'clear': 1.0,
      'rain': 1.3,
      'snow': 1.6,
      'fog': 1.4
    }[formData.weatherCondition];

    const predictedVolume = Math.round(baseTraffic.volume * weatherMultiplier);
    const predictedSpeed = Math.round(baseTraffic.speed / weatherMultiplier);
    const estimatedTime = Math.round((15.2 / predictedSpeed) * 60); // Assuming 15.2km route

    setPrediction({
      predictedVolume,
      predictedSpeed,
      estimatedTime,
      congestionLevel: predictedVolume > 350 ? 'High' : predictedVolume > 250 ? 'Medium' : 'Low',
      confidence: Math.round(85 + Math.random() * 10),
      weatherFactor: Math.round((weatherMultiplier - 1) * 100),
      recommendations: [
        predictedVolume > 350 ? 'Consider alternative routes' : 'Primary route looks good',
        weatherMultiplier > 1.2 ? 'Allow extra time due to weather' : 'Normal travel time expected',
        hour >= 7 && hour <= 9 ? 'Peak morning hours - expect delays' : 'Off-peak travel time'
      ]
    });
    
    setLoading(false);
  };

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const getTrafficColor = (level) => {
    switch(level) {
      case 'High': return 'text-red-600 bg-red-100';
      case 'Medium': return 'text-yellow-600 bg-yellow-100';
      case 'Low': return 'text-green-600 bg-green-100';
      default: return 'text-gray-600 bg-gray-100';
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <div className="bg-white shadow-lg border-b-4 border-blue-500">
        <div className="max-w-7xl mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="bg-blue-600 p-3 rounded-xl shadow-lg">
                <TrendingUp className="w-8 h-8 text-white" />
              </div>
              <div>
                <h1 className="text-3xl font-bold text-gray-900">Urban Traffic Flow Predictor</h1>
                <p className="text-gray-600">AI-powered traffic forecasting and route optimization</p>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-6 text-sm">
              <div className="text-center">
                <div className="text-2xl font-bold text-blue-600">{currentStats.averageSpeed}</div>
                <div className="text-gray-500">Avg Speed (km/h)</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-purple-600">{currentStats.congestionLevel}%</div>
                <div className="text-gray-500">Congestion</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-green-600">{currentStats.activeVehicles.toLocaleString()}</div>
                <div className="text-gray-500">Active Vehicles</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="max-w-7xl mx-auto px-4 py-6">
        <div className="flex space-x-1 bg-gray-100 p-1 rounded-xl mb-8">
          {[
            { id: 'predict', label: 'Traffic Prediction', icon: TrendingUp },
            { id: 'routes', label: 'Route Optimization', icon: Navigation },
            { id: 'analytics', label: 'Traffic Analytics', icon: BarChart }
          ].map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center space-x-2 px-6 py-3 rounded-lg font-medium transition-all ${
                activeTab === tab.id 
                  ? 'bg-white text-blue-600 shadow-md' 
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              <tab.icon className="w-5 h-5" />
              <span>{tab.label}</span>
            </button>
          ))}
        </div>

        {/* Traffic Prediction Tab */}
        {activeTab === 'predict' && (
          <div className="grid lg:grid-cols-2 gap-8">
            {/* Input Form */}
            <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
              <h2 className="text-xl font-bold text-gray-900 mb-6 flex items-center">
                <MapPin className="w-6 h-6 text-blue-600 mr-2" />
                Trip Details
              </h2>
              
              <div className="space-y-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">From</label>
                  <input
                    type="text"
                    name="startLocation"
                    value={formData.startLocation}
                    onChange={handleInputChange}
                    placeholder="Enter starting location"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">To</label>
                  <input
                    type="text"
                    name="endLocation"
                    value={formData.endLocation}
                    onChange={handleInputChange}
                    placeholder="Enter destination"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Departure Time</label>
                  <input
                    type="datetime-local"
                    name="departureTime"
                    value={formData.departureTime}
                    onChange={handleInputChange}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Weather Condition</label>
                  <select
                    name="weatherCondition"
                    value={formData.weatherCondition}
                    onChange={handleInputChange}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="clear">Clear</option>
                    <option value="rain">Rain</option>
                    <option value="snow">Snow</option>
                    <option value="fog">Fog</option>
                  </select>
                </div>
                
                <button
                  onClick={generatePrediction}
                  disabled={loading || !formData.startLocation || !formData.endLocation}
                  className="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white py-3 px-6 rounded-lg font-semibold hover:from-blue-700 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                >
                  {loading ? (
                    <div className="flex items-center justify-center">
                      <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                      Analyzing Traffic...
                    </div>
                  ) : (
                    'Predict Traffic'
                  )}
                </button>
              </div>
            </div>

            {/* Prediction Results */}
            <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
              <h2 className="text-xl font-bold text-gray-900 mb-6 flex items-center">
                <TrendingUp className="w-6 h-6 text-green-600 mr-2" />
                Traffic Prediction
              </h2>
              
              {prediction ? (
                <div className="space-y-6">
                  <div className="grid grid-cols-2 gap-4">
                    <div className="bg-blue-50 p-4 rounded-lg border border-blue-200">
                      <div className="text-3xl font-bold text-blue-600">{prediction.predictedVolume}</div>
                      <div className="text-sm text-blue-700">Vehicles/Hour</div>
                    </div>
                    <div className="bg-green-50 p-4 rounded-lg border border-green-200">
                      <div className="text-3xl font-bold text-green-600">{prediction.predictedSpeed}</div>
                      <div className="text-sm text-green-700">km/h Avg Speed</div>
                    </div>
                    <div className="bg-purple-50 p-4 rounded-lg border border-purple-200">
                      <div className="text-3xl font-bold text-purple-600">{prediction.estimatedTime}</div>
                      <div className="text-sm text-purple-700">Minutes ETA</div>
                    </div>
                    <div className="bg-gray-50 p-4 rounded-lg border border-gray-200">
                      <div className="text-3xl font-bold text-gray-600">{prediction.confidence}%</div>
                      <div className="text-sm text-gray-700">Confidence</div>
                    </div>
                  </div>

                  <div className="space-y-3">
                    <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                      <span className="font-medium text-gray-700">Congestion Level:</span>
                      <span className={`px-3 py-1 rounded-full text-sm font-medium ${getTrafficColor(prediction.congestionLevel)}`}>
                        {prediction.congestionLevel}
                      </span>
                    </div>
                    
                    {prediction.weatherFactor > 0 && (
                      <div className="flex items-center justify-between p-3 bg-orange-50 rounded-lg border border-orange-200">
                        <span className="font-medium text-orange-700 flex items-center">
                          <Cloud className="w-4 h-4 mr-2" />
                          Weather Impact:
                        </span>
                        <span className="text-orange-600 font-semibold">+{prediction.weatherFactor}% delay</span>
                      </div>
                    )}
                  </div>

                  <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
                    <h3 className="font-semibold text-yellow-800 flex items-center mb-3">
                      <AlertTriangle className="w-5 h-5 mr-2" />
                      AI Recommendations
                    </h3>
                    <ul className="space-y-2">
                      {prediction.recommendations.map((rec, index) => (
                        <li key={index} className="text-yellow-700 text-sm flex items-start">
                          <span className="w-2 h-2 bg-yellow-400 rounded-full mt-2 mr-3 flex-shrink-0"></span>
                          {rec}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              ) : (
                <div className="text-center py-12 text-gray-500">
                  <Car className="w-16 h-16 mx-auto mb-4 text-gray-300" />
                  <p className="text-lg">Enter trip details to get traffic prediction</p>
                  <p className="text-sm mt-2">Our AI model analyzes historical patterns, weather, and real-time data</p>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Route Optimization Tab */}
        {activeTab === 'routes' && (
          <div className="space-y-6">
            <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
              <h2 className="text-xl font-bold text-gray-900 mb-6 flex items-center">
                <Route className="w-6 h-6 text-green-600 mr-2" />
                Optimal Route Suggestions
              </h2>
              
              <div className="space-y-4">
                {routeData.map((route, index) => (
                  <div key={index} className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
                    <div className="flex items-center justify-between mb-3">
                      <h3 className="font-semibold text-lg text-gray-900">{route.route}</h3>
                      <span className={`px-3 py-1 rounded-full text-sm font-medium ${getTrafficColor(route.traffic)}`}>
                        {route.traffic} Traffic
                      </span>
                    </div>
                    
                    <div className="grid grid-cols-3 gap-4 text-sm">
                      <div className="text-center">
                        <div className="font-semibold text-blue-600">{route.distance}</div>
                        <div className="text-gray-500">Distance</div>
                      </div>
                      <div className="text-center">
                        <div className="font-semibold text-purple-600">{route.time}</div>
                        <div className="text-gray-500">Est. Time</div>
                      </div>
                      <div className="text-center">
                        <div className="font-semibold text-green-600">{route.fuel}</div>
                        <div className="text-gray-500">Fuel Est.</div>
                      </div>
                    </div>
                    
                    <button className="w-full mt-4 bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition-colors">
                      Select Route
                    </button>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Analytics Tab */}
        {activeTab === 'analytics' && (
          <div className="space-y-6">
            <div className="grid md:grid-cols-2 gap-6">
              <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
                <h3 className="text-lg font-semibold text-gray-900 mb-4">Traffic Volume Throughout Day</h3>
                <ResponsiveContainer width="100%" height={300}>
                  <LineChart data={historicalData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="time" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="volume" stroke="#3B82F6" strokeWidth={3} />
                  </LineChart>
                </ResponsiveContainer>
              </div>

              <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
                <h3 className="text-lg font-semibold text-gray-900 mb-4">Average Speed Analysis</h3>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={historicalData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="time" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Bar dataKey="speed" fill="#10B981" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">Congestion Patterns</h3>
              <div className="grid grid-cols-8 gap-2">
                {historicalData.map((data, index) => (
                  <div key={index} className="text-center">
                    <div className="text-xs text-gray-600 mb-2">{data.time}</div>
                    <div 
                      className={`h-16 rounded-lg flex items-end justify-center text-white font-bold text-xs ${
                        data.congestion === 'High' ? 'bg-red-500' :
                        data.congestion === 'Medium' ? 'bg-yellow-500' : 'bg-green-500'
                      }`}
                      style={{height: `${(data.volume / 500) * 100}px`}}
                    >
                      {data.volume}
                    </div>
                  </div>
                ))}
              </div>
              <div className="flex justify-center mt-4 space-x-6 text-sm">
                <div className="flex items-center">
                  <div className="w-4 h-4 bg-green-500 rounded mr-2"></div>
                  <span>Low Traffic</span>
                </div>
                <div className="flex items-center">
                  <div className="w-4 h-4 bg-yellow-500 rounded mr-2"></div>
                  <span>Medium Traffic</span>
                </div>
                <div className="flex items-center">
                  <div className="w-4 h-4 bg-red-500 rounded mr-2"></div>
                  <span>High Traffic</span>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8 mt-16">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <p className="text-gray-300">
            Urban Traffic Flow Predictor - Powered by Machine Learning & Real-time Data
          </p>
          <p className="text-gray-500 text-sm mt-2">
            Built with React, TensorFlow, and modern web technologies
          </p>
        </div>
      </footer>
    </div>
  );
};

export default TrafficPredictor;
