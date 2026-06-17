# MIC_STAT_SYSTEM_PREF

> This statistical reference table contains the system preference information defined for a service resource.

**Description:** Micro Statistical System Preferences  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIOCHEMICAL_IND` | DOUBLE |  |  | This field indicates if biochemicals are to be abstracted. 0 = biochemicals are not to be abstracted. 1 = biochemicals are to be abstracted. |
| 2 | `FREETEXT_IND` | DOUBLE |  |  | This field indicates if workcard free textis to be abstracted. 0 = workcard free textis not to be abstracted. 1 = workcard free textis to be abstracted. |
| 3 | `NEGATIVE_PROCEDURE_IND` | DOUBLE |  |  | This field indicates if negative or positive procedures are to be abstracted. 0 = negative procedures are not to be abstracted. 1 = negative procedures are to be abstracted. |
| 4 | `OVERLAY_IND` | DOUBLE |  |  | This field indicates if reports are to be abstracted using overlay. 0 = reports are to be abstracted not using overlay. 1 = reports are to be abstracted using overlay. |
| 5 | `PERFORMED_BIO_IND` | DOUBLE |  |  | This field indicates if performed biochemicals are to be abstracted. 0 = performed biochemicals are not to be abstracted. 1 = performed biochemicals are to be abstracted. If the value is 1 in this field, the value should also be 1 in biochemical_ind field. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the service resource used to define system preference. The service resources are only at Institutions and Departments level. |
| 7 | `STAIN_REPORT_IND` | DOUBLE |  |  | This field indicates if stain reports are to be abstracted. 0 = stain reports are not to be abstracted. 1 = stain reports are to be abstracted. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

