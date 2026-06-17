# SN_PROC_SEG_ASSOCIATION

> All associated segments of procedures are stored in this table. A new row will be inserted into this table when user checks a segment under the procedure in SNDBProcMgr. A new row will be deleted when user unchecks a segment under the procedure in SNDBProcMgr.

**Description:** PROCEDURE_SEGMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Catalog code of a procedure that identifies a single row on the surgical_procedures table |
| 2 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type associated with this documentation segment, i.e. OR Nursing Record, Preop Nursing Assessment |
| 3 | `SEG_CD` | DOUBLE | NOT NULL |  | The segment associated with the procedure |
| 4 | `SN_PROC_SEG_ASSOCIATION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SN_PROC_SEG_ASSOCIATION table. |
| 5 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this documentation segment. Identified by a CDF Meaning of ""SURGAREA"" on the Service Resource codeset. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

