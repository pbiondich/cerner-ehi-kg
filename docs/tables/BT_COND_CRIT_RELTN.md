# BT_COND_CRIT_RELTN

> Contains information about how a charge group condition is related with al the criteria defined in the charge group condition tool.

**Description:** Bill Template Condition Criteria Relation  
**Table type:** REFERENCE  
**Primary key:** `BT_COND_CRIT_R_ID`  
**Columns:** 16  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BT_CONDITION_ID` | DOUBLE | NOT NULL | FK→ | This column relates this record to a specific Bill Template Condition record. |
| 7 | `BT_COND_CRIT_R_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a specific relationship between a Bill Template Condition and a Criteria record. |
| 8 | `BT_COND_LOGIC_IND` | DOUBLE | NOT NULL |  | Indicates whether a criteria is associated with any relational or logical operator defined in a charge group condition rule. |
| 9 | `BT_CRITERIA_CAT_ID` | DOUBLE | NOT NULL | FK→ | This column relates this record to a specific Criteria Catalog record. |
| 10 | `BT_SUB_CRITERIA_CD` | DOUBLE |  |  | This is the code value from the given code set 4002352 that allows multiple values for sub criteria value. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BT_CONDITION_ID` | [BT_CONDITION](BT_CONDITION.md) | `BT_CONDITION_ID` |
| `BT_CRITERIA_CAT_ID` | [BT_CRITERIA_CATALOG](BT_CRITERIA_CATALOG.md) | `BT_CRITERIA_CAT_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [BT_COND_CRIT_GRP_RELTN](BT_COND_CRIT_GRP_RELTN.md) | `BT_COND_CRIT_R_ID` |
| [BT_CRITERIA_LIMIT](BT_CRITERIA_LIMIT.md) | `BT_COND_CRIT_R_ID` |
| [BT_PRSNL_GRP_RELTN](BT_PRSNL_GRP_RELTN.md) | `BT_COND_CRIT_R_ID` |
| [CODE_VAL_GRP_RELTN](CODE_VAL_GRP_RELTN.md) | `BT_COND_CRIT_R_ID` |
| [HP_GROUP_RELTN](HP_GROUP_RELTN.md) | `BT_COND_CRIT_R_ID` |
| [NOMEN_GROUP_RELTN](NOMEN_GROUP_RELTN.md) | `BT_COND_CRIT_R_ID` |
| [ORG_GROUP_RELTN](ORG_GROUP_RELTN.md) | `BT_COND_CRIT_R_ID` |
| [PFT_BILL_ITEM_COND_CRIT_RELTN](PFT_BILL_ITEM_COND_CRIT_RELTN.md) | `BT_COND_CRIT_R_ID` |
| [TEXT_COND_CRIT_RELTN](TEXT_COND_CRIT_RELTN.md) | `BT_COND_CRIT_R_ID` |

