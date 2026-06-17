# BT_COND_CRIT_GRP_RELTN

> Stores the required information to save or evaluate a rule created in charge group condition tool

**Description:** Charge Condition Group Criteria Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the Account Table |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILLING_ENTITY_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the BILLING_ENTITY table. |
| 8 | `BILL_ITEM_ID` | DOUBLE |  | FK→ | Uniquely identifies a related row on the BILL_ITEM table. |
| 9 | `BT_CONDITION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely Identifies the related row on the BT_CONDITION table. |
| 10 | `BT_COND_CRIT_GRP_RELTN_ID` | DOUBLE | NOT NULL |  | System generated number to uniquely identify a row on the BT_COND_CRIT_GRP_RELTN table. |
| 11 | `BT_COND_CRIT_R_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the BT_COND_CRIT_R table. |
| 12 | `BT_CRITERIA_CAT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the BT_CRITERIA_CATALOG table. |
| 13 | `CODE_VALUE` | DOUBLE |  |  | This is the code value from the given code set that allows multiple values. |
| 14 | `COND_VALUE_DT_TM` | DATETIME |  |  | Contains the date and time value for the respective criteria. |
| 15 | `COND_VALUE_IND` | DOUBLE |  |  | Contains the condition value for indicator sub critieria category. |
| 16 | `CRITERIA_GROUP_NBR` | DOUBLE |  |  | Determines the group of criteria values selected. |
| 17 | `CRITERIA_SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the object within a collection. |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `HEALTH_PLAN_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row to the HEALTH_PLAN table. |
| 20 | `INTERFACE_FILE_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the interface_file table. |
| 21 | `LIMIT_TYPE_CD` | DOUBLE |  |  | code value for a specific type of limit from code set 21757 (Ex: age, balance etc.) |
| 22 | `LIMIT_VAL_TYPE_CD` | DOUBLE |  |  | code value for a specific value of limit from code set 21758(Ex: Days, Months, Financial Units etc) |
| 23 | `LOGICAL_OPERATOR_CD` | DOUBLE |  |  | Determines the logical operator assigned to a criteria in the rule |
| 24 | `LWR_LIMIT_VALUE` | DOUBLE |  |  | Lower Limit Value of limit value type specified |
| 25 | `NOMENCLATURE_ID` | DOUBLE |  | FK→ | This is the unique primary identifier from the nomenclature table for a corresponding bill code |
| 26 | `ORGANIZATION_ID` | DOUBLE |  | FK→ | Uniquely identifies the related organization on the organization table to which the Billing Entity is related. |
| 27 | `ORG_TYPE_CD` | DOUBLE |  |  | Type of organization from code set 278 |
| 28 | `PRSNL_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the PRSNL table. |
| 29 | `RELATIONAL_OPERATOR_CD` | DOUBLE | NOT NULL |  | Determines the relation operator assigned to a criteria in the rule. |
| 30 | `SOURCE_VOCAB_CD` | DOUBLE |  |  | Source Vocabulary for a specific patient code from code set 400 (Ex: ICD10) |
| 31 | `TEXT_COND_CRIT_CD` | DOUBLE |  |  | Code value for any free text crieria definition curently used for CDM code value. |
| 32 | `TEXT_COND_CRIT_TXT` | VARCHAR(200) |  |  | Value for any free text criteria definition currently used for CDM code value. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPR_LIMIT_VALUE` | DOUBLE |  |  | Upper Limit Value of limit value type specified |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `BT_CONDITION_ID` | [BT_CONDITION](BT_CONDITION.md) | `BT_CONDITION_ID` |
| `BT_COND_CRIT_R_ID` | [BT_COND_CRIT_RELTN](BT_COND_CRIT_RELTN.md) | `BT_COND_CRIT_R_ID` |
| `BT_CRITERIA_CAT_ID` | [BT_CRITERIA_CATALOG](BT_CRITERIA_CATALOG.md) | `BT_CRITERIA_CAT_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `INTERFACE_FILE_ID` | [INTERFACE_FILE](INTERFACE_FILE.md) | `INTERFACE_FILE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

