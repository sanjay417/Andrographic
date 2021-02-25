import React, {Component} from 'react';
import * as d3 from "d3";
class BarChart extends Component {
    constructor(){
        super();
        this.state = {
            graphData: [35,42,67,89,25,34,67,85]
        }

    }


    drawChart() {
        const  models = this.props.data;
        if (models && models.length > 0) {
            const data =  this.state.graphData;
            if (data.length > 0) {
                const w = 500, h = 500;
                const svg = d3.select('#'+ this.props.attributes.elem)
                    .append("svg")
                    .attr("width", w)
                    .attr("height", h)
                    .style("margin-left", 1);

                svg.selectAll("rect")
                    .data(data)
                    .enter()
                    .append("rect")
                    .attr("x", (d, i) => i * 30)
                    .attr("y", (d, i) => h - 10 * d)
                    .attr("width", 20)
                    .attr("height", (d, i) => d * 10)
                    .attr("fill", "sandybrown")
            }
        }
    }

    render(){
        this.drawChart();
        return <div id={"#" + this.props.id}></div>
    }
}

export default BarChart;
