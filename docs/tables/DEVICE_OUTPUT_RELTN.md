# DEVICE_OUTPUT_RELTN

> Relates Devices with document profiles

**Description:** DEVICE PROFILE RELATION  
**Table type:** REFERENCE  
**Primary key:** `DEVICE_OUTPUT_RELTN_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | When this value is set, the output_content_type_cd is the default for the selected device. |
| 2 | `DEVICE_CD` | DOUBLE | NOT NULL | FK→ | Device code to be related to a output_content_cd. this value comes from the DEVICE table and is not a true CODE_VALUE. |
| 3 | `DEVICE_OUTPUT_RELTN_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 4 | `ENVELOPE_PROCESS_CD` | DOUBLE | NOT NULL |  | Dictates how documents sent to repositories will be processed through this relationship |
| 5 | `OUTPUT_CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | These are the document types that are related to the selected devices. This can also be thought of as output content Code. |
| 6 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The Template ID used by CDG to build the dataset for transformation (FK from CR_REPORT_TEMPLATE) |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEVICE_CD` | [DEVICE](DEVICE.md) | `DEVICE_CD` |
| `TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DEVICE_OUTPUT_RELTN_R](DEVICE_OUTPUT_RELTN_R.md) | `DEVICE_OUTPUT_RELTN_ID` |

