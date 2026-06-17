# UCMR_CHARGE_ORDERABLE

> Stores reference data of professional charge orderables that can be associated with a Helix case type.

**Description:** Unified Case Manager Reference - Charge Orderable  
**Table type:** REFERENCE  
**Primary key:** `UCMR_CHARGE_ORDERABLE_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ASSIGNMENT_CD` | DOUBLE | NOT NULL |  | Indicates whether to assign the accession number of the case or the workup during activity time. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog code for the charge orders' orderable. |
| 3 | `DEF_RENDERING_PHYS_ID` | DOUBLE | NOT NULL |  | The person identifier of the default rendering physician of the charge orderable. |
| 4 | `DEF_SERVICE_DATE_CD` | DOUBLE | NOT NULL |  | Codeset value of when the service date shall be (e.g. Collected Date or Verified Date) |
| 5 | `UCMR_CHARGE_ORDERABLE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies professional charge orderables that can be associated with a Helix case type. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UCMR_CASE_CHARGE_ORDRBL_R](UCMR_CASE_CHARGE_ORDRBL_R.md) | `UCMR_CHARGE_ORDERABLE_ID` |

