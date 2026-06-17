# SCH_WARN_TYPE

> Scheduling Warning Types

**Description:** Scheduling Warning Types  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. The information-only text is used by the client to document the database. |
| 10 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 11 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 12 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 13 | `REASON_ACCEPT_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the reason accept option. |
| 14 | `REASON_ACCEPT_MEANING` | VARCHAR(12) | NOT NULL |  | Th 12-character description corresponding to the scheduling reason accept code. |
| 15 | `STARTER_DATA_IND` | DOUBLE | NOT NULL |  | Starter Data Indicator |
| 16 | `TEMPLATE_ACCEPT_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling accept option. |
| 17 | `TEMPLATE_ACCEPT_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling accept code. |
| 18 | `TEXT_ACCEPT_CD` | DOUBLE | NOT NULL | FK→ | The coded indentifer for the scheduling text accept option. |
| 19 | `TEXT_ACCEPT_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling accept code. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date and time this version of the current record becomes historical. |
| 26 | `WARN_LEVEL_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling warning level. |
| 27 | `WARN_LEVEL_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponding to the schedulingwarning level. |
| 28 | `WARN_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the scheduling warning type. |
| 29 | `WARN_TYPE_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponding to the schedulingwarning type code. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INFO_SCH_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REASON_ACCEPT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TEMPLATE_ACCEPT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TEXT_ACCEPT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_LEVEL_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

