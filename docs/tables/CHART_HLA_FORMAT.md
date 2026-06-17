# CHART_HLA_FORMAT

> Chart HLA Format

**Description:** This table defines attributes in Chart HLA section.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABO_RH_LABEL` | VARCHAR(32) |  |  | The label for ABO column. |
| 2 | `ABO_RH_ORDER` | DOUBLE |  |  | The order for ABO column. |
| 3 | `ABO_RPT` | DOUBLE |  |  | The repeat indicator for ABO column label. |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Chart group id. The foreign key value from CHART_GROUP |
| 9 | `DATE_LABEL` | VARCHAR(32) |  |  | The label for collected date column. |
| 10 | `DATE_ORDER` | DOUBLE |  |  | The order for collected date column. |
| 11 | `DATE_RPT` | DOUBLE |  |  | The repeat indicator for collected date column label. |
| 12 | `HAPLOID1_LABEL` | VARCHAR(32) |  |  | The label for Haplotype ID 1 column. |
| 13 | `HAPLOID1_ORDER` | DOUBLE |  |  | The order for Haplotype ID 1 column. |
| 14 | `HAPLOID2_LABEL` | VARCHAR(32) |  |  | The label for Haplotype ID 2 column. |
| 15 | `HAPLOID2_ORDER` | DOUBLE |  |  | The order for Haplotype ID 2 column. |
| 16 | `HAPLOTYPE1_LABEL` | VARCHAR(32) |  |  | The label for Haplotype result 1 column. |
| 17 | `HAPLOTYPE1_ORDER` | DOUBLE |  |  | The order for Haplotype result 1 column. |
| 18 | `HAPLOTYPE2_LABEL` | VARCHAR(32) |  |  | The label for Haplotype result 2 column. |
| 19 | `HAPLOTYPE2_ORDER` | DOUBLE |  |  | The order for Haplotype result 2 column. |
| 20 | `HLA_TYPE` | DOUBLE |  |  | The type of HLA section. 0 -- HLA Typing. 1 -- HLA Haplotype. |
| 21 | `LINE_INDICATOR` | DOUBLE |  |  | The indicator for results pair printed in one line or two lines. |
| 22 | `MRN_LABEL` | VARCHAR(32) |  |  | The label for MRN column. |
| 23 | `MRN_ORDER` | DOUBLE |  |  | The order for MRN column. |
| 24 | `MRN_RPT` | DOUBLE |  |  | The repeat indicator for MRN column label. |
| 25 | `PRSN_NAME_LABEL` | VARCHAR(32) |  |  | The label for person name column. |
| 26 | `PRSN_NAME_ORDER` | DOUBLE |  |  | The order for person name column. |
| 27 | `PRSN_NAME_RPT` | DOUBLE |  |  | The repeat indicator for person name column label. |
| 28 | `RELATION_LABEL` | VARCHAR(32) |  |  | The label for relationship column. |
| 29 | `RELATION_ORDER` | DOUBLE |  |  | The order for relationship column. |
| 30 | `RELATION_RPT` | DOUBLE |  |  | The repeat indicator for relationship column label. |
| 31 | `RESULT_ORDER` | DOUBLE |  |  | The order for HLA typing result column. |
| 32 | `RESULT_SEQ_FLAG` | DOUBLE |  |  | The flag for sorting results. |
| 33 | `RH_IND` | DOUBLE | NOT NULL |  | Indicator for displaying RH with ABO on a chart |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

