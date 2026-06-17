# SCH_REPORT

> Scheduling Report

**Description:** Scheduling Report  
**Table type:** REFERENCE  
**Primary key:** `SCH_REPORT_ID`  
**Columns:** 29  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADVANCED_IND` | DOUBLE |  |  | Determines if the inquiry/report is using the advanged inquiry/reporting logic. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 8 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 13 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 14 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 15 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 16 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 17 | `OE_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the accept format. |
| 18 | `POSTSCRIPT_IND` | DOUBLE | NOT NULL |  | This field is used to determine if the scheduling report is a ASCII or POSTSCRIPT. |
| 19 | `PROGRAM_NAME` | VARCHAR(30) |  |  | The CCL program name to execute. |
| 20 | `REPORT_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling report type. |
| 21 | `REPORT_RETEN_DAY_CNT` | DOUBLE | NOT NULL |  | The number of days that a report job is to remain in a completed state before being archived. |
| 22 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling report type. |
| 23 | `SCH_REPORT_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the scheduling report. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `OE_FORMAT_ID` | [ORDER_ENTRY_FORMAT_PARENT](ORDER_ENTRY_FORMAT_PARENT.md) | `OE_FORMAT_ID` |
| `REPORT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [EEM_ABN_FORM](EEM_ABN_FORM.md) | `EEM_REPORT_ID` |
| [EEM_PROFILE_REPORT](EEM_PROFILE_REPORT.md) | `SCH_REPORT_ID` |
| [SCH_ACTION_NOTIFY](SCH_ACTION_NOTIFY.md) | `SCH_REPORT_ID` |
| [SCH_NOTIFY](SCH_NOTIFY.md) | `SCH_REPORT_ID` |
| [SCH_ROUTE_LIST](SCH_ROUTE_LIST.md) | `SCH_REPORT_ID` |

