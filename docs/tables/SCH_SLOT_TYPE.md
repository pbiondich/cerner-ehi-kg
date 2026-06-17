# SCH_SLOT_TYPE

> The slot type is associated with slot to specify the type of appointments that can utilize the slot.

**Description:** Slot Types  
**Table type:** REFERENCE  
**Primary key:** `SLOT_TYPE_ID`  
**Columns:** 30  
**Referenced by:** 13 columns

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
| 7 | `CONTIGUOUS_IND` | DOUBLE |  |  | Determines if a slot type is defined to be contiguous or discrete. |
| 8 | `DEF_DURATION` | DOUBLE |  |  | The default amount of time (in minutes) for this slot type. |
| 9 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 10 | `DISP_SCHEME_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the display scheme. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `GROUP_CAPACITY_DEFAULT_QTY` | DOUBLE | NOT NULL |  | The default group capacity for inpatient group appointments. |
| 13 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 14 | `INTERVAL` | DOUBLE |  |  | Time interval that the apptointments within the slot should start at |
| 15 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 16 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 17 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 18 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 19 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 20 | `NON_SCHEDULE_IND` | DOUBLE | NOT NULL |  | To indicate that the slot type is not schedulable. 1 = Not Schedulable. |
| 21 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 22 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | priority code value |
| 23 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling flex string. |
| 24 | `SLOT_TYPE_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the slot type. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISP_SCHEME_ID` | [SCH_DISP_SCHEME](SCH_DISP_SCHEME.md) | `DISP_SCHEME_ID` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |

## Referenced by (13)

| From table | Column |
|------------|--------|
| [BR_SCH_TEMP_SLOT_RELEASE_R](BR_SCH_TEMP_SLOT_RELEASE_R.md) | `RELEASE_TYPE_ID` |
| [SCH_ACTION_ROLE](SCH_ACTION_ROLE.md) | `SLOT_TYPE_ID` |
| [SCH_APPT](SCH_APPT.md) | `SCH_TYPE_ID` |
| [SCH_APPT](SCH_APPT.md) | `SLOT_TYPE_ID` |
| [SCH_APPT_DEF](SCH_APPT_DEF.md) | `SLOT_TYPE_ID` |
| [SCH_CAB_SLOT](SCH_CAB_SLOT.md) | `SLOT_TYPE_ID` |
| [SCH_DEF_SLOT](SCH_DEF_SLOT.md) | `SLOT_TYPE_ID` |
| [SCH_EVENT_RECUR_ROLE](SCH_EVENT_RECUR_ROLE.md) | `SLOT_TYPE_ID` |
| [SCH_EVENT_ROLE](SCH_EVENT_ROLE.md) | `SLOT_TYPE_ID` |
| [SCH_LIST_SLOT](SCH_LIST_SLOT.md) | `SLOT_TYPE_ID` |
| [SCH_SLOT_LIST](SCH_SLOT_LIST.md) | `SLOT_TYPE_ID` |
| [SN_SURG_CASE_ST](SN_SURG_CASE_ST.md) | `ACTUAL_SLOT_TYPE_ID` |
| [SN_SURG_CASE_ST](SN_SURG_CASE_ST.md) | `SCH_SLOT_TYPE_ID` |

