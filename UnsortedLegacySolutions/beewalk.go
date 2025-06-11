package main

import (
	"fmt"
)

type Cell struct {
	curr int64
	prev int64
}

func withinBounds(i int, j int) bool {
	if (i > 0) && (j > 0) && (i < 40) && (j < 40) {
		return true
	} else {
		return false
	}
}

func walk(steps int) int64 {
	grid := make([][]*Cell, 40)
	for i := 0; i < len(grid); i++ {
		grid[i] = make([]*Cell, 40)
		for j := 0; j < 40; j++ {
			grid[i][j] = &Cell{0, 0}
		}
	}
	//there is 1 way to get to central cell with 0 steps
	grid[19][19] = &Cell{1, 1}
	//l represents the steps taken -1
	for l := 0; l < steps; l++ {
		//for all cells make previous value the current value and make current value 0
		for i := 0; i < len(grid); i++ {
			j := 0
			if i%2 != 0 {
				j = 1
			}
			for j < len(grid[0]) {
				grid[i][j].prev = grid[i][j].curr
				grid[i][j].curr = 0
				j += 2
			}
		}
		//for all cells make current value the sum of all its neighbours
		for i := 0; i < len(grid); i++ {
			j := 0
			if i%2 != 0 {
				j = 1
			}
			for j < len(grid[0]) {
				if withinBounds(i+1, j+1) {
					grid[i][j].curr += grid[i+1][j+1].prev
				}
				if withinBounds(i+1, j-1) {
					grid[i][j].curr += grid[i+1][j-1].prev
				}
				if withinBounds(i-1, j+1) {
					grid[i][j].curr += grid[i-1][j+1].prev
				}
				if withinBounds(i-1, j-1) {
					grid[i][j].curr += grid[i-1][j-1].prev
				}
				if withinBounds(i+2, j) {
					grid[i][j].curr += grid[i+2][j].prev
				}
				if withinBounds(i-2, j) {
					grid[i][j].curr += grid[i-2][j].prev
				}
				j += 2
			}
		}
	}
	return grid[19][19].curr
}

func main() {
	//formats input
	numberWalks := 0
	fmt.Scanf("%d\n", &numberWalks)
	walks := make([]int, numberWalks)
	scanningCurrently := 0
	for i := 0; i < numberWalks; i++ {
		fmt.Scanf("%d\n", &scanningCurrently)
		walks[i] = scanningCurrently
	}
	for i := 0; i < len(walks); i++ {
		fmt.Println(walk(walks[i]))
	}
}
