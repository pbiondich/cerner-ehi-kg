# RC_GSR_DIMENSION_TMP

> This table is used by the GSR dimension load process to identify the distinct set of rows in each of the dimension tables which must be inserted or updated during the current job execution. This table does not need a unique PK value or associated index.

**Description:** Revenue Cycle Gold Standard Reporting Dimension Temporary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL |  | A sequential batch identifier assigned to a group of rows inserted into this table by the GSR dimension load process for the logical_domain_id in which the process is being executed. |
| 2 | `DIM_INDEX` | DOUBLE | NOT NULL |  | This field is an index into the recDWItems structure that is used by the GSR dimension load process to access the parameters needed to process the loading of data for each dimension table |
| 3 | `INSERT_IND` | DOUBLE | NOT NULL |  | This field will be set to 0 if the dimension row related to this row already exists and must be updated, or 1 if a new row will need to be inserted. |
| 4 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 5 | `LONG_TEXT_MD5_HASH_TXT` | VARCHAR(32) | NOT NULL |  | This field is a unique identifier based on the value of the long_text string that is linked to the referenced rc_cln_area row. While rc_cln_area may include large numbers of rows that reference the same dimension row, only one row will be inserted into this table for each distinct dimension row based on the value of this column. |
| 6 | `RCR_GSR_CONTEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the RCR_GSR_CONTEXT table. |
| 7 | `RC_CLN_AREA_ID` | DOUBLE | NOT NULL |  | This is the primary key of a row on the rc_cln_area staging table. |
| 8 | `RC_DIMENSION_ID` | DOUBLE | NOT NULL |  | This field is a numeric identifier that is associated with each GSR dimension table. The specific values assigned to each dimension table are defined in the pft_load_dw.inc include file. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCR_GSR_CONTEXT_ID` | [RCR_GSR_CONTEXT](RCR_GSR_CONTEXT.md) | `RCR_GSR_CONTEXT_ID` |

