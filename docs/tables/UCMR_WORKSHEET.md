# UCMR_WORKSHEET

> This table stores reference data for a protocol worksheet.

**Description:** Unified Case Manager Worksheet  
**Table type:** REFERENCE  
**Primary key:** `UCMR_WORKSHEET_ID`  
**Columns:** 12  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `UCMR_WORKSHEET_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies a row on the UCMR_WORKSHEET table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `WORKSHEET_NAME_CD` | DOUBLE | NOT NULL |  | The code value of the worksheet name. |
| 12 | `XML_FORMATTING_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores worksheet formatting information in an xml blob. This information may include input section, process section, output section flags or any other information pertaining to the worksheet. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `XML_FORMATTING_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [UCMR_POSITION_MAP](UCMR_POSITION_MAP.md) | `UCMR_WORKSHEET_ID` |
| [UCMR_WORKSHEET_ORDERABLE_R](UCMR_WORKSHEET_ORDERABLE_R.md) | `UCMR_WORKSHEET_ID` |
| [UCMR_WORKSHEET_STATEMENT_R](UCMR_WORKSHEET_STATEMENT_R.md) | `UCMR_WORKSHEET_ID` |
| [UCM_PTL_BATCH](UCM_PTL_BATCH.md) | `UCMR_WORKSHEET_ID` |

