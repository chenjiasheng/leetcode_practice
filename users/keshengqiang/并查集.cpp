int parent[100];
int size;

void Init()
{
    for (int i = 0; i < 100; i++) {
	    parent[i] = i;
	}
}

int find(int x)
{
    if (parent[x] != x) {
        parent[x] = find(parent[x]);
	}
	return parent[x];
}

void union(int x, int y)
{
    int root_x = find(x);
	int root_y = find(y);
	
	if (root_x != root_y) {
	    parent[root_x] = root_y;
	}
}