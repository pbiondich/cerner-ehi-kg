# SCH_FLEX_STRING

> Scheduling Flex String

**Description:** Scheduling Flex String  
**Table type:** REFERENCE  
**Primary key:** `SCH_FLEX_ID`  
**Columns:** 24  
**Referenced by:** 22 columns

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
| 7 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FLEX_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the flexing type. |
| 10 | `FLEX_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the flexing type. |
| 11 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 14 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 15 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 16 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 17 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 18 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the scheduling flex string. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FLEX_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (22)

| From table | Column |
|------------|--------|
| [ENCNTR_SLICE_REFERENCE](ENCNTR_SLICE_REFERENCE.md) | `SCH_FLEX_ID` |
| [PFT_RULESET_FLEX_RELTN](PFT_RULESET_FLEX_RELTN.md) | `SCH_FLEX_ID` |
| [PM_POST_DOC_REF](PM_POST_DOC_REF.md) | `SCH_FLEX_ID` |
| [PRSNL_GROUP_POOL](PRSNL_GROUP_POOL.md) | `SCH_FLEX_ID` |
| [PRSNL_GROUP_POOL_ROUTING_R](PRSNL_GROUP_POOL_ROUTING_R.md) | `SCH_FLEX_ID` |
| [SCH_ACTION_NOTIFY](SCH_ACTION_NOTIFY.md) | `SCH_FLEX_ID` |
| [SCH_APPT_ACTION](SCH_APPT_ACTION.md) | `SCH_FLEX_ID` |
| [SCH_APPT_DEF](SCH_APPT_DEF.md) | `SCH_FLEX_ID` |
| [SCH_APPT_LOC](SCH_APPT_LOC.md) | `SCH_FLEX_ID` |
| [SCH_APPT_NOTIFY](SCH_APPT_NOTIFY.md) | `SCH_FLEX_ID` |
| [SCH_APPT_ROUTING](SCH_APPT_ROUTING.md) | `SCH_FLEX_ID` |
| [SCH_DEF_SLOT](SCH_DEF_SLOT.md) | `SCH_FLEX_ID` |
| [SCH_FLEX_LIST](SCH_FLEX_LIST.md) | `SCH_FLEX_ID` |
| [SCH_LIST_RES](SCH_LIST_RES.md) | `SCH_FLEX_ID` |
| [SCH_LIST_ROLE](SCH_LIST_ROLE.md) | `SCH_FLEX_ID` |
| [SCH_LIST_SLOT](SCH_LIST_SLOT.md) | `SCH_FLEX_ID` |
| [SCH_ORDER_APPT](SCH_ORDER_APPT.md) | `SCH_FLEX_ID` |
| [SCH_ORDER_DURATION](SCH_ORDER_DURATION.md) | `SCH_FLEX_ID` |
| [SCH_ORDER_ROLE](SCH_ORDER_ROLE.md) | `SCH_FLEX_ID` |
| [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SCH_FLEX_ID` |
| [SCH_SUB_LIST](SCH_SUB_LIST.md) | `SCH_FLEX_ID` |
| [SN_SURG_CASE_ST](SN_SURG_CASE_ST.md) | `SCH_FLEX_ID` |

