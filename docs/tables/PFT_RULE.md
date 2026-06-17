# PFT_RULE

> This table contains top-level information for each rule (i.e. type, name, description, etc.)

**Description:** PFT Rule  
**Table type:** REFERENCE  
**Primary key:** `RULE_ID`  
**Columns:** 23  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | The date that the record was created in the table. |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for inserting this row on the table |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `OBJECT_NAME` | VARCHAR(100) |  |  | Name of the object to be used in place of rule defined through tool. |
| 11 | `RULE_DESC` | VARCHAR(100) |  |  | Description of the rule. |
| 12 | `RULE_ID` | DOUBLE | NOT NULL | PK | Unique ID for rule. |
| 13 | `RULE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Logical string used in script to avoid regeneration upon each claim generation. |
| 14 | `RULE_NAME` | VARCHAR(50) | NOT NULL |  | Name of the rule. |
| 15 | `RULE_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Sub-type of rule (i.e. HCFA Standard, State Regulatory, etc.) |
| 16 | `RULE_TYPE_CD` | DOUBLE | NOT NULL |  | Type of rule (i.e. HCFA 1450: Condition Codes, HCFA 1500, etc.) |
| 17 | `STANDARD_IND` | DOUBLE | NOT NULL |  | Indicator for whether or not the rule was defined by Cerner as a standard rule. |
| 18 | `STATE_CD` | DOUBLE | NOT NULL |  | State for which rule is defined. Used only for State Regulatory rules. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `RULE_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PFT_RULE_ACTION](PFT_RULE_ACTION.md) | `RULE_ID` |
| [PFT_RULE_GROUP](PFT_RULE_GROUP.md) | `RULE_ID` |

