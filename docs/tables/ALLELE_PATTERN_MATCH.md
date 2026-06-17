# ALLELE_PATTERN_MATCH

> Records the alleles identified in HLA molecular gel testing as determined by pattern matching or as entered by the user for a specific order and gel.

**Description:** Allele Pattern Match  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLELE_CD` | DOUBLE | NOT NULL |  | The code for an allele identified as a result of testing using an HLA molecular typing gel. |
| 2 | `GEL_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Identifies which gel batch this gel is associated with. It is a foreign key reference to the primary key of the gel_batch table. |
| 3 | `GEL_NUMBER` | DOUBLE | NOT NULL | FK→ | A number which identifies the gel to which the allele result relates. It is a foreign key reference to the primary key of the gel table. |
| 4 | `LOCI_CD` | DOUBLE | NOT NULL |  | The code for the HLA Loci where the allele is located. |
| 5 | `LOCI_SEQ` | DOUBLE | NOT NULL |  | Arbitrarily assigned number to make each record unique. This is necessary since the same Loci Code and Allele Code may be used more than once. Also determines the order of display. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates the allele to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GEL_BATCH_ID` | [GEL_LOADING](GEL_LOADING.md) | `GEL_BATCH_ID` |
| `GEL_NUMBER` | [GEL_LOADING](GEL_LOADING.md) | `GEL_NUMBER` |
| `ORDER_ID` | [GEL_LOADING](GEL_LOADING.md) | `ORDER_ID` |

