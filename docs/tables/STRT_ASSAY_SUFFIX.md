# STRT_ASSAY_SUFFIX

> Contains suffix's to an assay alias.

**Description:** Contains suffix's to an assay alias  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DNLD_SUFFIX` | CHAR(15) |  |  | The suffix to the assay alias |
| 3 | `STRT_ASSAY_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned key field value from strt_assay table. |
| 4 | `STRT_MODEL_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned key field value from strt_model table. |
| 5 | `STRT_SUFFIX_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned key. |
| 6 | `SUFFIX_DESC` | CHAR(50) |  |  | Contains the description of the suffix |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `UPLD_SUFFIX` | CHAR(15) |  |  | Contains the upload suffix to the alias |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

