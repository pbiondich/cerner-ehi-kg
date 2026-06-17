# SCH_DEF_SCHED

> The default schedule defined the planned workload of a resource.

**Description:** Scheduling Default Schedules  
**Table type:** REFERENCE  
**Primary key:** `DEF_SCHED_ID`  
**Columns:** 29  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLY_RANGE` | DOUBLE |  |  | Application Range |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BEG_TM` | DOUBLE | NOT NULL |  | Defines the standard start time. |
| 8 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 9 | `DEFAULT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the default schedule type. |
| 10 | `DEFAULT_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the default schedule type. |
| 11 | `DEF_SCHED_ID` | DOUBLE | NOT NULL | PK | The identifier for a default schedule. |
| 12 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 13 | `DURATION` | DOUBLE |  |  | The duration in minutes. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `END_TM` | DOUBLE | NOT NULL |  | Defines the standard ending time. |
| 16 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 17 | `INTERVAL` | DOUBLE | NOT NULL |  | Defines the time interval in minutes. |
| 18 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 19 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 20 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 21 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 22 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 23 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
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
| `DEFAULT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [SCH_APPLY_LIST](SCH_APPLY_LIST.md) | `DEF_SCHED_ID` |
| [SCH_DATE_SET](SCH_DATE_SET.md) | `DEF_SCHED_ID` |
| [SCH_DEF_APPLY](SCH_DEF_APPLY.md) | `DEF_SCHED_ID` |
| [SCH_DEF_LOC_R](SCH_DEF_LOC_R.md) | `DEF_SCHED_ID` |
| [SCH_DEF_RES](SCH_DEF_RES.md) | `DEF_SCHED_ID` |
| [SCH_DEF_SLOT](SCH_DEF_SLOT.md) | `DEF_SCHED_ID` |

