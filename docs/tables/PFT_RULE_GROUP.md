# PFT_RULE_GROUP

> This table contains information concerning the grouping of qualifications

**Description:** PFT RULE GROUP  
**Table type:** REFERENCE  
**Primary key:** `GROUP_ID`  
**Columns:** 20  
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
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `GROUP_DESC` | VARCHAR(100) |  |  | Description of the group. |
| 10 | `GROUP_ID` | DOUBLE | NOT NULL | PK | Unique ID for the group. |
| 11 | `GROUP_NAME` | VARCHAR(50) | NOT NULL |  | Name of the group. |
| 12 | `GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | Determines the associated rule group type. |
| 13 | `PARENT_GROUP_NBR` | DOUBLE | NOT NULL |  | Group NBR of group's parent group (if any). |
| 14 | `RULE_ID` | DOUBLE | NOT NULL | FK→ | Rule ID of rule to which the group belongs. |
| 15 | `TABLE_CD` | DOUBLE | NOT NULL |  | Table identifier links qualifications together. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RULE_ID` | [PFT_RULE](PFT_RULE.md) | `RULE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PFT_RULE_QUALIFICATION](PFT_RULE_QUALIFICATION.md) | `GROUP_ID` |
| [PFT_RULE_TABLE_QUAL](PFT_RULE_TABLE_QUAL.md) | `RULE_GROUP_ID` |

