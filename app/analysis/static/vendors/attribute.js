function show_figure3(data) {
    var myChart = echarts.init(document.getElementById('vis_dis'));
        var schema = [
            {name: 'AGE', index: 0, text: 'Age'},
            {name: 'Blood Pressure', index: 1, text: 'Blood Pressure'},
            {name: 'Amount', index: 2, text: 'Amount'}
        ];
        var option = {
            backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
            offset: 0,
            color: '#f7f8fa'}, 
            {
                offset: 1,
                color: '#cdd0d5'
            }]),
            legend: {
                right: 10,
                data: ['Male', 'Female']
                
            },
            tooltip: {
                padding: 10,
                backgroundColor: '#222',
                borderColor: '#777',
                borderWidth: 1,
                formatter: function (obj) {
                    var value = obj.value;
                    return  schema[0].text + ': ' + value[0] + '<br>'
                        + schema[1].text + '：' + value[1] + '<br>'
                        + schema[2].text + '：' + value[2] + '<br>';
                }
            },
            xAxis: {
                min:25,
                name: 'Ages',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                }
            },
            yAxis: {
                name: 'Resting Blood Pressure',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                },
                scale: true
            },
            series: [{
                name: 'Male',
                data: data[0],
                type: 'scatter',
                symbolSize: function (data) {
                    return Math.sqrt(data[2]) / 0.15;
                },
                itemStyle: {
                    normal: {
                        shadowBlur: 10,
                        shadowColor: 'rgba(120, 36, 50, 0.5)',
                        shadowOffsetY: 5,
                        color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                            offset: 0,
                            color: 'rgb(251, 118, 123)'
                        }, {
                            offset: 1,
                            color: 'rgb(204, 46, 72)'
                        }])
                    }
                }
            }, {
                name: 'Female',
                data: data[1],
                type: 'scatter',
                symbolSize: function (data) {
                    return Math.sqrt(data[2]) / 0.15;
                },
                itemStyle: {
                    normal: {
                        shadowBlur: 10,
                        shadowColor: 'rgba(25, 100, 150, 0.5)',
                        shadowOffsetY: 5,
                        color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                            offset: 0,
                            color: 'rgb(129, 227, 238)'
                        }, {
                            offset: 1,
                            color: 'rgb(25, 183, 207)'
                        }])
                    }
                }
            }]
        };
        myChart.setOption(option, true);

}

function show_figure4(data) {
    console.log("4444444")
    var myChart = echarts.init(document.getElementById('vis_dis'));             
    var redata={"x": ["0-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-100"], "male": data[0], "female": data[1]}
    var option = {
            tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
    },
    legend: {
        data: ['typical angin', 'atypical angina','non-anginal','asymptomatic'],
        y: '90%'
        
    },

    title: [{
        text: 'Male',
        x: '25%',
        textAlign: 'center'
    }, {
        text: 'Female',
        x: '75%',
        textAlign: 'center'
    }],


    grid: [
        {x: '7%', y: '7%', width: '38%', height: '75%'},
        {x2: '7%', y: '7%', width: '38%', height: '75%'}
    ],
    xAxis:  [{
        //interval: 0,
        //offset:45,
        gridIndex:0,
        name: 'Ages',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000},
        type: 'category',
        data: redata['x'],
        axisLabel:{rotate:45}
    },{
        //interval: 0,
        //offset:45,
        gridIndex:1,
        name: 'Ages',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000},
        type: 'category',
        data: redata['x'],
        axisLabel:{rotate:45}
    }],
    yAxis: [{
        type: 'value',
        gridIndex:0,
        name: 'Amount',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000}
        
    },
    {gridIndex:1,type: 'value',
    name: 'Amount',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000}}],
    series: [
        {
            name: 'typical angin',
            type: 'bar',
            stack: 'total',
            xAxisIndex: 0,
            yAxisIndex: 0,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['male'][0]

        },
        {
            name: 'atypical angina',
            type: 'bar',
            stack: 'total',
            xAxisIndex: 0,
            yAxisIndex: 0,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['male'][1]

        },
        {
            name: 'non-anginal',
            type: 'bar',
            stack: 'total',
            xAxisIndex: 0,
            yAxisIndex: 0,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['male'][2]

        },
        {
            name: 'asymptomatic',
            type: 'bar',
            stack: 'total',
            xAxisIndex: 0,
            yAxisIndex: 0,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['male'][3]
        },{
            name: 'typical angin',
            type: 'bar',
            stack: 'total1',
            xAxisIndex: 1,
            yAxisIndex: 1,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['female'][0]

        },
        {
            name: 'atypical angina',
            type: 'bar',
            stack: 'total1',
            xAxisIndex: 1,
            yAxisIndex: 1,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['female'][1]

        },
        {
            name: 'non-anginal',
            type: 'bar',
            stack: 'total1',
            xAxisIndex: 1,
            yAxisIndex: 1,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['female'][2]

        },
        {
            name: 'asymptomatic',
            type: 'bar',
            stack: 'total1',
            xAxisIndex: 1,
            yAxisIndex: 1,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['female'][3]

        }
    ]
        };

        
        myChart.setOption(option, true);
}


function show_figure5(data) {
    var myChart = echarts.init(document.getElementById('vis_dis'));
        var schema = [
            {name: 'AGE', index: 0, text: 'Age'},
            {name: 'Blood Pressure', index: 1, text: 'serum cholestoral in mg/dl'},
            {name: 'Amount', index: 2, text: 'Amount'}
        ];
        var option = {
            backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
            offset: 0,
            color: '#f7f8fa'}, 
            {
                offset: 1,
                color: '#cdd0d5'
            }]),
            legend: {
                right: 10,
                data: ['Male', 'Female']
            },
            tooltip: {
                padding: 10,
                backgroundColor: '#222',
                borderColor: '#777',
                borderWidth: 1,
                formatter: function (obj) {
                    var value = obj.value;
                    return  schema[0].text + ': ' + value[0] + '<br>'
                        + schema[1].text + '：' + value[1] + '<br>'
                        + schema[2].text + '：' + value[2] + '<br>';
                }
            },
            xAxis: {
                min:25,
                name: 'Ages',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                }
            },
            yAxis: {
                name: 'serum cholestoral in mg/dl',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                },
                scale: true
            },
            series: [{
                name: 'Male',
                data: data[0],
                type: 'scatter',
                symbolSize: function (data) {
                    return Math.sqrt(data[2]) / 0.15;
                },
                itemStyle: {
                    normal: {
                        shadowBlur: 10,
                        shadowColor: 'rgba(120, 36, 50, 0.5)',
                        shadowOffsetY: 5,
                        color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                            offset: 0,
                            color: 'rgb(251, 118, 123)'
                        }, {
                            offset: 1,
                            color: 'rgb(204, 46, 72)'
                        }])
                    }
                }
            }, {
                name: 'Female',
                data: data[1],
                type: 'scatter',
                symbolSize: function (data) {
                    return Math.sqrt(data[2]) / 0.15;
                },
                itemStyle: {
                    normal: {
                        shadowBlur: 10,
                        shadowColor: 'rgba(25, 100, 150, 0.5)',
                        shadowOffsetY: 5,
                        color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                            offset: 0,
                            color: 'rgb(129, 227, 238)'
                        }, {
                            offset: 1,
                            color: 'rgb(25, 183, 207)'
                        }])
                    }
                }
            }]
        };
        myChart.setOption(option, true);

}

function show_figure6(data) {
    var myChart = echarts.init(document.getElementById('vis_dis'));             
    var redata={"x": ["0-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-100"], "male": data[0], "female": data[1]}
    var option = {
            tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
    },
    legend: {
        data: ['True', 'False'],
        y: '90%'
    },

    title: [{
        text: 'Male',
        x: '25%',
        textAlign: 'center'
    }, {
        text: 'Female',
        x: '75%',
        textAlign: 'center'
    }],


    grid: [
        {x: '7%', y: '7%', width: '38%', height: '75%'},
        {x2: '7%', y: '7%', width: '38%', height: '75%'}
    ],
    xAxis:  [{
        //interval: 0,
        //offset:45,
        gridIndex:0,
        name: 'Ages',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000},
        type: 'category',
        data: redata['x'],
        axisLabel:{rotate:45}
    },{
        //interval: 0,
        //offset:45,
        gridIndex:1,
        name: 'Ages',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000},
        type: 'category',
        data: redata['x'],
        axisLabel:{rotate:45}
    }],
    yAxis: [{
        type: 'value',
        gridIndex:0,
        name: 'Amount',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000}
        
    },
    {gridIndex:1,type: 'value',
    name: 'Amount',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000}}],
    series: [
        {
            name: 'True',
            type: 'bar',
            stack: 'total',
            xAxisIndex: 0,
            yAxisIndex: 0,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['male'][0]

        },
        {
            name: 'False',
            type: 'bar',
            stack: 'total',
            xAxisIndex: 0,
            yAxisIndex: 0,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['male'][1]

        },{
            name: 'True',
            type: 'bar',
            stack: 'total1',
            xAxisIndex: 1,
            yAxisIndex: 1,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['female'][0]

        },
        {
            name: 'False',
            type: 'bar',
            stack: 'total1',
            xAxisIndex: 1,
            yAxisIndex: 1,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['female'][1]

        }
    ]
        };

        
        myChart.setOption(option, true);
}

function show_figure7(data) {
    var myChart = echarts.init(document.getElementById('vis_dis'));             
    var redata={"x": ["0-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-100"], "male": data[0], "female": data[1]}
    var option = {
            tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
    },
    legend: {
        data: ['Normal', 'Having ST-T wave abnormality', 'showing probable or definite left ventricular hypertrophy by Estes’ criteria'],
        y: '90%'
    },

    title: [{
        text: 'Male',
        x: '25%',
        textAlign: 'center'
    }, {
        text: 'Female',
        x: '75%',
        textAlign: 'center'
    }],


    grid: [
        {x: '7%', y: '7%', width: '38%', height: '75%'},
        {x2: '7%', y: '7%', width: '38%', height: '75%'}
    ],
    xAxis:  [{
        //interval: 0,
        //offset:45,
        gridIndex:0,
        name: 'Ages',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000},
        type: 'category',
        data: redata['x'],
        axisLabel:{rotate:45}
    },{
        //interval: 0,
        //offset:45,
        gridIndex:1,
        name: 'Ages',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000},
        type: 'category',
        data: redata['x'],
        axisLabel:{rotate:45}
    }],
    yAxis: [{
        type: 'value',
        gridIndex:0,
        name: 'Amount',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000}
        
    },
    {gridIndex:1,type: 'value',
    name: 'Amount',
        nameLocation: 'end',
        nameTextStyle:{fontWeight:1000}}],
    series: [
        {
            name: 'typical angin',
            type: 'bar',
            stack: 'total',
            xAxisIndex: 0,
            yAxisIndex: 0,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['male'][0]

        },
        {
            name: 'atypical angina',
            type: 'bar',
            stack: 'total',
            xAxisIndex: 0,
            yAxisIndex: 0,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['male'][1]

        },
        {
            name: 'non-anginal',
            type: 'bar',
            stack: 'total',
            xAxisIndex: 0,
            yAxisIndex: 0,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['male'][2]

        },{
            name: 'typical angin',
            type: 'bar',
            stack: 'total1',
            xAxisIndex: 1,
            yAxisIndex: 1,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['female'][0]

        },
        {
            name: 'atypical angina',
            type: 'bar',
            stack: 'total1',
            xAxisIndex: 1,
            yAxisIndex: 1,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['female'][1]

        },
        {
            name: 'non-anginal',
            type: 'bar',
            stack: 'total1',
            xAxisIndex: 1,
            yAxisIndex: 1,
            label: {
                normal: {
                    show: true,
                    position: 'insideRight'
                }
            },
            data: redata['female'][2]

        }
    ]
        };

        
        myChart.setOption(option, true);
}

function show_figure8(data) {
    var myChart = echarts.init(document.getElementById('vis_dis'));
        var schema = [
            {name: 'AGE', index: 0, text: 'Age'},
            {name: 'Blood Pressure', index: 1, text: 'maximum heart rate achieved'},
            {name: 'Amount', index: 2, text: 'Amount'}
        ];
        var option = {
            backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
            offset: 0,
            color: '#f7f8fa'}, 
            {
                offset: 1,
                color: '#cdd0d5'
            }]),
            legend: {
                right: 10,
                data: ['Male', 'Female']
            },
            tooltip: {
                padding: 10,
                backgroundColor: '#222',
                borderColor: '#777',
                borderWidth: 1,
                formatter: function (obj) {
                    var value = obj.value;
                    return  schema[0].text + ': ' + value[0] + '<br>'
                        + schema[1].text + '：' + value[1] + '<br>'
                        + schema[2].text + '：' + value[2] + '<br>';
                }
            },
            xAxis: {
                min:25,
                name: 'Ages',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                }
            },
            yAxis: {
                name: 'maximum heart rate achieved',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                splitLine: {
                    lineStyle: {
                        type: 'dashed'
                    }
                },
                scale: true
            },
            series: [{
                name: 'Male',
                data: data[0],
                type: 'scatter',
                symbolSize: function (data) {
                    return Math.sqrt(data[2]) / 0.15;
                },
                itemStyle: {
                    normal: {
                        shadowBlur: 10,
                        shadowColor: 'rgba(120, 36, 50, 0.5)',
                        shadowOffsetY: 5,
                        color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                            offset: 0,
                            color: 'rgb(251, 118, 123)'
                        }, {
                            offset: 1,
                            color: 'rgb(204, 46, 72)'
                        }])
                    }
                }
            }, {
                name: 'Female',
                data: data[1],
                type: 'scatter',
                symbolSize: function (data) {
                    return Math.sqrt(data[2]) / 0.15;
                },
                itemStyle: {
                    normal: {
                        shadowBlur: 10,
                        shadowColor: 'rgba(25, 100, 150, 0.5)',
                        shadowOffsetY: 5,
                        color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                            offset: 0,
                            color: 'rgb(129, 227, 238)'
                        }, {
                            offset: 1,
                            color: 'rgb(25, 183, 207)'
                        }])
                    }
                }
            }]
        };
        myChart.setOption(option, true);

}
function attribute9(data){
    var myChart = echarts.init(document.getElementById('vis_dis'));
        var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male": data[0], "female": data[1]}
        var option = {
            tooltip : {
            trigger: 'axis',
            axisPointer : {            
                type : 'shadow'        
            }
            },
            legend: {
                data: ['exercise induced angina:False', 'exercise induced angina:True'],
                y: '90%'
            },

            title: [{
                text: 'Male',
                x: '25%',
                textAlign: 'center'
            }, {
                text: 'Female',
                x: '75%',
                textAlign: 'center'
            }],


            grid: [
                {x: '7%', y: '7%', width: '38%', height: '75%'},
                {x2: '7%', y: '7%', width: '38%', height: '75%'}
            ],
            xAxis:  [{
                gridIndex:0,
                name: 'Ages',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                type: 'category',
                data: redata['x'],
                axisLabel:{rotate:45}
            },{
                gridIndex:1,
                name: 'Ages',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                type: 'category',
                data: redata['x'],
                axisLabel:{rotate:45}
            }],
            yAxis: [{
                type: 'value',
                gridIndex:0,
                name: 'Amount',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000}
                
            },
            {gridIndex:1,type: 'value',
            name: 'Amount',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000}}],
            series: [
                {
                    name: 'exercise induced angina:False',
                    type: 'bar',
                    stack: 'total',
                    xAxisIndex: 0,
                    yAxisIndex: 0,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: redata['male'][0]

                },
                {
                    name: 'exercise induced angina:True',
                    type: 'bar',
                    stack: 'total',
                    xAxisIndex: 0,
                    yAxisIndex: 0,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: redata['male'][1]

                },
                {
                    name: 'exercise induced angina:False',
                    type: 'bar',
                    stack: 'total1',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: redata['female'][0]

                },
                {
                    name: 'exercise induced angina:True',
                    type: 'bar',
                    stack: 'total1',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: redata['female'][1]

                }
            ]
        };
        myChart.setOption(option, true);
}

function attribute10(data){
    var myChart = echarts.init(document.getElementById('vis_dis'));
    var schema = [
        {name: 'AGE', index: 0, text: 'Age'},
        {name: 'Blood Pressure', index: 1, text: 'oldpeak'},
        {name: 'Amount', index: 2, text: 'Amount'}
    ];
    var option = {
        backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
        offset: 0,
        color: '#f7f8fa'}, 
        {
            offset: 1,
            color: '#cdd0d5'
        }]),
        legend: {
            right: 10,
            data: ['Male', 'Female']
        },
        tooltip: {
            padding: 10,
            backgroundColor: '#222',
            borderColor: '#777',
            borderWidth: 1,
            formatter: function (obj) {
                var value = obj.value;
                return  schema[0].text + ': ' + value[0] + '<br>'
                    + schema[1].text + '：' + value[1] + '<br>'
                    + schema[2].text + '：' + value[2] + '<br>';
            }
        },
        xAxis: {
            min:25,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            splitLine: {
                lineStyle: {
                    type: 'dashed'
                }
            }
        },
        yAxis: {
            name: 'oldpeak',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            splitLine: {
                lineStyle: {
                    type: 'dashed'
                }
            },
            scale: true
        },
        series: [{
            name: 'Male',
            data: data[0],
            type: 'scatter',
            symbolSize: function (data) {
                return Math.sqrt(data[2]) / 0.15;
            },
            itemStyle: {
                normal: {
                    shadowBlur: 10,
                    shadowColor: 'rgba(120, 36, 50, 0.5)',
                    shadowOffsetY: 5,
                    color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                        offset: 0,
                        color: 'rgb(251, 118, 123)'
                    }, {
                        offset: 1,
                        color: 'rgb(204, 46, 72)'
                    }])
                }
            }
        }, {
            name: 'Female',
            data: data[1],
            type: 'scatter',
            symbolSize: function (data) {
                return Math.sqrt(data[2]) / 0.15;
            },
            itemStyle: {
                normal: {
                    shadowBlur: 10,
                    shadowColor: 'rgba(25, 100, 150, 0.5)',
                    shadowOffsetY: 5,
                    color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                        offset: 0,
                        color: 'rgb(129, 227, 238)'
                    }, {
                        offset: 1,
                        color: 'rgb(25, 183, 207)'
                    }])
                }
            }
        }]
    };
    myChart.setOption(option, true);

}

function attribute11(data){
    var myChart = echarts.init(document.getElementById('vis_dis'));
    var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male": data[0], "female": data[1]}
    var option = {
        tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
        },
        legend: {
            data: ['the slope of the peak exercise ST segment:1', 'the slope of the peak exercise ST segment:2','the slope of the peak exercise ST segment:3'],
            y: '90%'
        },

        title: [{
            text: 'Male',
            x: '25%',
            textAlign: 'center'
        }, {
            text: 'Female',
            x: '75%',
            textAlign: 'center'
        }],


        grid: [
            {x: '7%', y: '7%', width: '38%', height: '75%'},
            {x2: '7%', y: '7%', width: '38%', height: '75%'}
        ],
        xAxis:  [{
            gridIndex:0,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        },{
            gridIndex:1,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        }],
        yAxis: [{
            type: 'value',
            gridIndex:0,
            name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}
            
        },
        {gridIndex:1,type: 'value',
        name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}}],
        series: [
            {
                name: 'the slope of the peak exercise ST segment:1',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][0]

            },
            {
                name: 'the slope of the peak exercise ST segment:2',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][1]

            },
            {
                name: 'the slope of the peak exercise ST segment:3',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][2]

            },
            {
                name: 'the slope of the peak exercise ST segment:1',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][0]

            },
            {
                name: 'the slope of the peak exercise ST segment:2',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][1]

            },
            {
                name: 'the slope of the peak exercise ST segment:3',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][2]

            }
            
        ]
    };
    myChart.setOption(option, true);
}

function attribute12(data){
    var myChart = echarts.init(document.getElementById('vis_dis'));
    var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male": data[0], "female": data[1]}
    var option = {
        tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
        },
        legend: {
            data: ['vessels colored:0', 'vessels colored:1','vessels colored:2','vessels colored:3'],
            y:'90%'
        },

        title: [{
            text: 'Male',
            x: '25%',
            textAlign: 'center'
        }, {
            text: 'Female',
            x: '75%',
            textAlign: 'center'
        }],


        grid: [
            {x: '7%', y: '7%', width: '38%', height: '75%'},
            {x2: '7%', y: '7%', width: '38%', height: '75%'}
        ],
        xAxis:  [{
            gridIndex:0,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        },{
            gridIndex:1,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        }],
        yAxis: [{
            type: 'value',
            gridIndex:0,
            name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}
            
        },
        {gridIndex:1,type: 'value',
        name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}}],
        series: [
            {
                name: 'vessels colored:0',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][0]

            },
            {
                name: 'vessels colored:1',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][1]

            },
            {
                name: 'vessels colored:2',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][2]

            },
            {
                name: 'vessels colored:3',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][3]
            },
            {
                name: 'vessels colored:0',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][0]

            },
            {
                name: 'vessels colored:1',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][1]

            },
            {
                name: 'vessels colored:2',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][2]

            },
            {
                name: 'vessels colored:3',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][3]

            }
        ]
    };
        myChart.setOption(option, true);
}


function attribute13(data){
    var myChart = echarts.init(document.getElementById('vis_dis'));
var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male": data[0], "female": data[1]}
    var option = {
        tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
        },
        legend: {
            data: ['thal: normal', 'thal: fixed defect','thal: reversable defect'],
            y: '90%'
        },

        title: [{
            text: 'Male',
            x: '25%',
            textAlign: 'center'
        }, {
            text: 'Female',
            x: '75%',
            textAlign: 'center'
        }],


        grid: [
            {x: '7%', y: '7%', width: '38%', height: '75%'},
            {x2: '7%', y: '7%', width: '38%', height: '75%'}
        ],
        xAxis:  [{
            gridIndex:0,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        },{
            gridIndex:1,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        }],
        yAxis: [{
            type: 'value',
            gridIndex:0,
            name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}
            
        },
        {gridIndex:1,type: 'value',
        name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}}],
        series: [
            {
                name: 'thal: normal',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][0]

            },
            {
                name: 'thal: fixed defect',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][1]

            },
            {
                name: 'thal: reversable defect',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][2]

            },
            {
                name: 'thal: normal',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][0]

            },
            {
                name: 'thal: fixed defect',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][1]

            },
            {
                name: 'thal: reversable defect',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][2]

            }
            
        ]
    };
    myChart.setOption(option, true);
}

function attribute14(data){
    var myChart = echarts.init(document.getElementById('vis_dis'));
    var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male":  data[0], "female": data[1]}
    var option = {
        tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
        },
        legend: {
            data: ['target: 0', 'target: 1','target: 2','target: 3','target: 4'],
            y: '90%'
        },

        title: [{
            text: 'Male',
            x: '25%',
            textAlign: 'center'
        }, {
            text: 'Female',
            x: '75%',
            textAlign: 'center'
        }],


        grid: [
            {x: '7%', y: '7%', width: '38%', height: '75%'},
            {x2: '7%', y: '7%', width: '38%', height: '75%'}
        ],
        xAxis:  [{
            gridIndex:0,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        },{
            gridIndex:1,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        }],
        yAxis: [{
            type: 'value',
            gridIndex:0,
            name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}
            
        },
        {gridIndex:1,type: 'value',
        name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}}],
        series: [
            {
                name: 'target: 0',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][0]

            },
            {
                name: 'target: 1',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][1]

            },
            {
                name: 'target: 2',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][2]

            },
            {
                name: 'target: 3',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][3]

            },
            {
                name: 'target: 4',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][4]

            },
            {
                name: 'target: 0',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][0]

            },
            {
                name: 'target: 1',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][1]

            },
            {
                name: 'target: 2',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][2]

            },
            {
                name: 'target: 3',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][3]

            },
            {
                name: 'target: 4',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][4]

            }
            
        ]
    };
    myChart.setOption(option, true);
}