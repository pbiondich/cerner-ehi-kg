# CDI_AC_FORMTYPE

> The CDI Ascent Capture Form Type table

**Description:** CDI Ascent Capture Form Type  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCHMODULEID` | VARCHAR(38) | NOT NULL |  | batch module identifier |
| 2 | `CDI_AC_FORMTYPE_ID` | DOUBLE | NOT NULL |  | cdi ascent capture formtype identifier |
| 3 | `COMPLETEDDOCS` | DOUBLE |  |  | completed docs |
| 4 | `COMPLETEDPAGES` | DOUBLE |  |  | completed pages |
| 5 | `DOCCLASSNAME` | VARCHAR(32) |  |  | doc class name |
| 6 | `DOCUMENTS` | DOUBLE |  |  | documents |
| 7 | `FORMTYPEENTRYID` | VARCHAR(38) | NOT NULL |  | form type entry identifier |
| 8 | `FORMTYPENAME` | VARCHAR(32) |  |  | form type name |
| 9 | `KS_BCREPAIR` | DOUBLE |  |  | ks bc repair |
| 10 | `KS_ICRREPAIR` | DOUBLE |  |  | ks icr repair |
| 11 | `KS_MANUAL` | DOUBLE |  |  | ks manual |
| 12 | `KS_OCRREPAIR` | DOUBLE |  |  | ks ocr repair |
| 13 | `KS_OMRREPAIR` | DOUBLE |  |  | ks omr repair |
| 14 | `PAGES` | DOUBLE |  |  | pages |
| 15 | `REJECTEDDOCS` | DOUBLE |  |  | rejected docs |
| 16 | `REJECTEDPAGES` | DOUBLE |  |  | rejected pages |
| 17 | `TRANSFERID` | VARCHAR(38) | NOT NULL |  | transfer identifier |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

