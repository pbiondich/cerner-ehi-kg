# CONTROL_MATERIAL

> Defines the control material for the Quality Control system

**Description:** Control Material  
**Table type:** REFERENCE  
**Primary key:** `CONTROL_ID`  
**Columns:** 12  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLIND_SAMPLE_IND` | DOUBLE |  |  | Indicates whether the material is defined for blind sampling. A value of 0 indicates the material is not defined for blind sampling. A value of 1 indicates the material is defined for blind sampling. (Currently not implemented) |
| 2 | `CONTROL_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific control material. |
| 3 | `CONTROL_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific control type, such as high, low, normal, and so on. |
| 4 | `DESCRIPTION` | VARCHAR(200) |  |  | Character description of the control material. |
| 5 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific control manufacturer. |
| 6 | `SHORT_DESCRIPTION` | VARCHAR(20) |  |  | Defines the short description of the control material for looking up a control. |
| 7 | `SHORT_DESC_KEY` | VARCHAR(20) |  |  | Defines the short description in uppercase with spaces and special characters removed. Used for sorting and checking the defined control materials. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (9)

| From table | Column |
|------------|--------|
| [CONTROL_LOT](CONTROL_LOT.md) | `CONTROL_ID` |
| [CONTROL_X_CHECK](CONTROL_X_CHECK.md) | `CONTROL_ID` |
| [QC_ALPHA_RESPONSES](QC_ALPHA_RESPONSES.md) | `CONTROL_ID` |
| [QC_GROUP_CTRL_RESOURCE](QC_GROUP_CTRL_RESOURCE.md) | `CONTROL_ID` |
| [QC_RESULT](QC_RESULT.md) | `CONTROL_ID` |
| [QC_SCHEDULE_CTRL](QC_SCHEDULE_CTRL.md) | `CONTROL_ID` |
| [QC_STAT_PERIOD](QC_STAT_PERIOD.md) | `CONTROL_ID` |
| [RESOURCE_ACCESSION_R](RESOURCE_ACCESSION_R.md) | `CONTROL_ID` |
| [RESOURCE_ASSAY_CONTROL](RESOURCE_ASSAY_CONTROL.md) | `CONTROL_ID` |

