# SCH_LIST_ROLE

> Scheduling List Role

**Description:** Scheduling List Role  
**Table type:** REFERENCE  
**Primary key:** `LIST_ROLE_ID`  
**Columns:** 41  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALGORITHM_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling algorithm. The scheduling algorithm detemines how resources are scheduled. |
| 6 | `ALGORITHM_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponding to the scheduling algorithm. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 9 | `CONCURRENT_IND` | DOUBLE | NOT NULL |  | an indicator to allow current role to book into the same resource as primary role in a concurrent slot |
| 10 | `DEFINING_IND` | DOUBLE |  |  | Determines if the role is the defining role. |
| 11 | `DEP_LIST_ROLE_ID` | DOUBLE | NOT NULL |  | The identifier of the dependent list role. |
| 12 | `DEP_RESOURCE_CD` | DOUBLE | NOT NULL |  | The coded identifier for the dependent resource. |
| 13 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 16 | `LIST_ROLE_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the scheduling role. |
| 17 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 18 | `MNEMONIC` | VARCHAR(100) |  |  | A 100-character string used for identification and selection. |
| 19 | `MNEMONIC_KEY` | VARCHAR(100) |  |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 20 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 21 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 22 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 23 | `OPTIONAL_IND` | DOUBLE |  |  | Determines if the scheduling relationship is required or optional. |
| 24 | `PRIMARY_IND` | DOUBLE |  |  | Mark the appointment synonym as the primary synonym for the appointment type. |
| 25 | `PROMPT_ACCEPT_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the prompt accept option. This field determines if the resource role should prompt the user for the valid resources. |
| 26 | `PROMPT_ACCEPT_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the prompt accept option. |
| 27 | `RESCH_PREV_RES_IND` | DOUBLE | NOT NULL |  | An indicator to show whether we will reschedule the appointment back the original scheduled resource. |
| 28 | `RES_LIST_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the scheduling resource list. |
| 29 | `ROLE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling role. |
| 30 | `ROLE_SEQ` | DOUBLE |  |  | The order of the role on the resource list. |
| 31 | `ROLE_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A internal identifier for the scheduling role type. |
| 32 | `ROLE_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling Role Type. |
| 33 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling flex string. |
| 34 | `SCH_ROLE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling role. |
| 35 | `SELECTED_IND` | DOUBLE |  |  | Determines if the object is (by default) selected or not. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 41 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALGORITHM_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PROMPT_ACCEPT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `RES_LIST_ID` | [SCH_RESOURCE_LIST](SCH_RESOURCE_LIST.md) | `RES_LIST_ID` |
| `ROLE_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |
| `SCH_ROLE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (12)

| From table | Column |
|------------|--------|
| [ITEM_CONTROL_INFO](ITEM_CONTROL_INFO.md) | `LIST_ROLE_ID` |
| [SCH_ACTION_ROLE](SCH_ACTION_ROLE.md) | `LIST_ROLE_ID` |
| [SCH_EVENT_RECUR_ROLE](SCH_EVENT_RECUR_ROLE.md) | `LIST_ROLE_ID` |
| [SCH_EVENT_ROLE](SCH_EVENT_ROLE.md) | `LIST_ROLE_ID` |
| [SCH_LIST_RES](SCH_LIST_RES.md) | `LIST_ROLE_ID` |
| [SCH_LIST_SLOT](SCH_LIST_SLOT.md) | `CLEANUP_ROLE_ID` |
| [SCH_LIST_SLOT](SCH_LIST_SLOT.md) | `DURATION_ROLE_ID` |
| [SCH_LIST_SLOT](SCH_LIST_SLOT.md) | `OFFSET_ROLE_ID` |
| [SCH_LIST_SLOT](SCH_LIST_SLOT.md) | `SETUP_ROLE_ID` |
| [SCH_ORDER_ROLE](SCH_ORDER_ROLE.md) | `LIST_ROLE_ID` |
| [SCH_PEND_APPT](SCH_PEND_APPT.md) | `LIST_ROLE_ID` |
| [SCH_PEND_SURG_ITEM](SCH_PEND_SURG_ITEM.md) | `LIST_ROLE_ID` |

