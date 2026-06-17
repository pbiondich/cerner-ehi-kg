# MIC_QC_BIO_TEST_RESULT

> Contains the biochemical results for a microbiology quality control organism

**Description:** Microbiology Quality Control Test Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_BIOCHEMICAL_CD` | DOUBLE | NOT NULL |  | The code set value that identifies the detail biochemical task associated with the row. (CS 1004) |
| 2 | `GROUP_BIOCHEMICAL_CD` | DOUBLE | NOT NULL |  | The code set value that identifies the group biochemical task associated with the row. (CS 1002) |
| 3 | `QC_ORGANISM_ID` | DOUBLE | NOT NULL | FK→ | Unique internal identification ID assigned to the ordered quality control organism. |
| 4 | `RESULT_CD` | DOUBLE | NOT NULL |  | Identifies the code value of the biochemical result. (CS 1027) |
| 5 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies the status of the biochemical result. (CS 1901) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QC_ORGANISM_ID` | [MIC_QC_ORGANISM](MIC_QC_ORGANISM.md) | `QC_ORGANISM_ID` |

