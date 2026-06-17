# SCH_REF_FREQ

> Scheduling Reference Ferquencies

**Description:** Scheduling Reference Frequencies  
**Table type:** REFERENCE  
**Primary key:** `REF_FREQ_ID`  
**Columns:** 32  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `DAYS_OF_WEEK` | VARCHAR(10) | NOT NULL |  | A character string used to store the valid days of the week. |
| 8 | `DAY_STRING` | VARCHAR(31) | NOT NULL |  | A character string used to store the valid days of the month. |
| 9 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FREQ_PATTERN_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the frequency pattern. |
| 12 | `FREQ_PATTERN_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the frequency pattern. |
| 13 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 14 | `INTERVAL` | DOUBLE | NOT NULL |  | Defines the time interval in minutes. |
| 15 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 16 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 17 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 18 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 19 | `MONTH_STRING` | VARCHAR(12) | NOT NULL |  | A string used to denote the valid months in a frequency. |
| 20 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 21 | `PATTERN_OPTION` | DOUBLE | NOT NULL |  | This field is used to store the frequency option chosen by the user. |
| 22 | `REF_FREQ_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the scheduling reference frequency. |
| 23 | `UNITS` | DOUBLE | NOT NULL |  | Units |
| 24 | `UNITS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier of the units of measure. |
| 25 | `UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the units of measure. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 31 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 32 | `WEEK_STRING` | VARCHAR(6) | NOT NULL |  | A character string used to denote the valid weeks within the month. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FREQ_PATTERN_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCH_FREQ](SCH_FREQ.md) | `REF_FREQ_ID` |

