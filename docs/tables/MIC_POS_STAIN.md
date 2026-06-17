# MIC_POS_STAIN

> This reference table contains a single record for every positive stain criteria included in the PathNet Microbiology system.

**Description:** Microbiology Positive Stain  
**Table type:** REFERENCE  
**Primary key:** `POS_STAIN_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | This field identifieds the internal identification code of body site to which the positive stain criteria is set up. |
| 2 | `POS_STAIN_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code that uniquely identifies the positive stain criteria (and it's associated parameters). This value is used to join to another table (mic_pos_stain_report). |
| 3 | `PROCEDURE_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the procedure used to define positive stains. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the service resource to which the positive stain criteria is assigned. This could be used to join to the service_resource table. |
| 5 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define positive stains. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_POS_STAIN_REPORT](MIC_POS_STAIN_REPORT.md) | `POS_STAIN_ID` |

