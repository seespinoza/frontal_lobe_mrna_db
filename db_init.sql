/*Create Frontal Lobe Database database */

CREATE TABLE expression_values (
    sample_id            integer,     --Unique RNA-seq sample ID from Allen Brain Atlas
    gene_symbol          varchar,     --Gene Symbol
    sub_structure        varchar,     --Frontal lobe substructure where sample was taken.
    raw_counts           integer      --Raw RNA-seq counts for a certain sample gene.
);

CREATE TABLE maps_to (
    gene                 varchar,     --Gene Symbol
    gene_id              integer,     --Gene ID
    sample_id            integer      --Unique RNA-seq sample ID from Allen Brain Atlas  
);

CREATE TABLE differentially_expressed_genes (
    gene_symbol          varchar,     --Gene Symbol
    gene_id              integer      --Gene ID
);

CREATE TABLE associated (
    gene_id              integer,     --Gene ID
    go_id                varchar      --Unique GO ID for the term associated with the gene
);

CREATE TABLE go_terms (
    go_id                varchar,     --Unique GO ID
    term                 varchar      --Name of GO term
);


/* Copy data. */
\copy expression_values FROM './data/expression_values.tsv' WITH NULL AS '-'
\copy maps_to FROM './data/maps_to' WITH NULL AS '-'
\copy differentially_expressed_genes FROM './data/differentially_expressed_genes.tsv' WITH NULL AS '-'
\copy associated FROM './data/associated.tsv' WITH NULL AS '-'
\copy go_terms FROM './data/go_terms.tsv' WITH NULL AS '-'
