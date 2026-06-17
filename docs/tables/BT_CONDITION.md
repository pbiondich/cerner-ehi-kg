# BT_CONDITION

> Contains Information about the Bill Template Condition

**Description:** Bill Template Condition  
**Table type:** REFERENCE  
**Primary key:** `BT_CONDITION_ID`  
**Columns:** 37  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTO_SUBMIT_CD` | DOUBLE | NOT NULL |  | The period of time to lapse before auto submit occurs |
| 6 | `AUTO_SUBMIT_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the group of charges identified by this condition should be submitted automatically on a bill |
| 7 | `AUTO_SUBMIT_VAL` | DOUBLE | NOT NULL |  | The amount of time to lapse before auto submit occurs |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BILLING_PERIOD_TYPE_CD` | DOUBLE | NOT NULL |  | Defines how often an insurance benefit order will bill (All, Monthly, Weekly, Daily) |
| 10 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | The type of bill for the condition |
| 11 | `BT_CONDITION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies each bill template condition. |
| 12 | `BT_CONDITION_TREE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the tree of bill template conditions. |
| 13 | `BT_COND_LOGIC_IND` | DOUBLE | NOT NULL |  | Indicates whether a criteria is associated with any relational or logical operator defined in a charge group condition rule. |
| 14 | `CONDITION_NAME` | VARCHAR(200) |  |  | Contains the name of a particular bill template condition. |
| 15 | `CONDITION_NAME_KEY` | VARCHAR(255) |  |  | Contains the name of a particular bill template condition. This column will be in all capitals with special characters and spaces removed. |
| 16 | `ENCNTR_TYPE_CLASS_CHRG_GRP_IND` | DOUBLE | NOT NULL |  | Indicates whether Charge grouping functionality for non-Inpatient encounters needs to be used or not. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `FOLLOW_UP_CD` | DOUBLE | NOT NULL |  | The period of time to lapse before follow up occurs |
| 19 | `FOLLOW_UP_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the group of charges identified by this condition should be followed up on before they are submitted on a bill |
| 20 | `FOLLOW_UP_VAL` | DOUBLE | NOT NULL |  | The amount of time to lapse before follow up occurs |
| 21 | `INTERVAL_DAYS` | DOUBLE | NOT NULL |  | Charges to be groupd based on Number of Interval days |
| 22 | `MAN_REVIEW_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the group of charges identified by this condition should be manually reviewed before being sent out on a bill |
| 23 | `PARENT_BT_COND_ID` | DOUBLE | NOT NULL | FK→ | A unique identifier indicating the parent of a bill template condition. |
| 24 | `PHYS_GROUPING_FLAG` | DOUBLE | NOT NULL |  | Physician grouping option at the bill template condition level. Indicates how to group professional charges 0 - group by performing physician 1 - group all together 2 - group by ordering physician 0 - default to how it is done today 1 - group all professional charges into one professional charge group 2 - group professional charges by ordering physician |
| 25 | `PRE_ADMIT_CHRG_DAYS` | DOUBLE | NOT NULL |  | Number of days prior to the admit date to be grouped separately. |
| 26 | `PRE_ADMIT_CHRG_IND` | DOUBLE | NOT NULL |  | Indicates whether charges prior to admit date time needs to be grouped separately. |
| 27 | `PRIORITY_SEQ` | DOUBLE |  |  | Sequence of related rows |
| 28 | `QUALIFYING_DT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Sotres the values for the different qualifying date types. |
| 29 | `REPROCESS_IND` | DOUBLE | NOT NULL |  | Stores the REPROCESS_IND value - The value is 1 - when user updated charge group manually in bt condition tool(this is used in charge group reprocessing tool), 0(default) if not |
| 30 | `SINGLE_CHRG_IND` | DOUBLE | NOT NULL |  | Indicates whether a charge group can contain only a single charge. A value of "1" indicates the charge group can contain only a single charge. A value of "0" indicates the charge group can contain multiple charges. |
| 31 | `SINGLE_CHRG_ROLL_IND` | DOUBLE | NOT NULL |  | Indicates whether a charge will roll to another when using single charge, charge groups. |
| 32 | `STD_DELAY_DAYS` | DOUBLE | NOT NULL |  | Defines a standard delay period in days for when a bill is to be submitted or transmitted. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BT_CONDITION_TREE_ID` | [BT_CONDITION_TREE](BT_CONDITION_TREE.md) | `BT_CONDITION_TREE_ID` |
| `PARENT_BT_COND_ID` | [BT_CONDITION](BT_CONDITION.md) | `BT_CONDITION_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [BENEFIT_ORDER](BENEFIT_ORDER.md) | `BT_CONDITION_ID` |
| [BT_CONDITION](BT_CONDITION.md) | `PARENT_BT_COND_ID` |
| [BT_COND_CRIT_GRP_RELTN](BT_COND_CRIT_GRP_RELTN.md) | `BT_CONDITION_ID` |
| [BT_COND_CRIT_RELTN](BT_COND_CRIT_RELTN.md) | `BT_CONDITION_ID` |
| [PFT_CHRG_GRP_RPRCS](PFT_CHRG_GRP_RPRCS.md) | `BT_CONDITION_ID` |
| [PFT_CHRG_GRP_RPRCS_HIST](PFT_CHRG_GRP_RPRCS_HIST.md) | `BT_CONDITION_ID` |

