# MM_APPROVAL

> Contains the different approval profiles.

**Description:** MM APPROVAL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPROVAL_AMOUNT` | DOUBLE |  |  | Amount up to which a person can approve. |
| 2 | `APPROVAL_LEVEL` | DOUBLE |  |  | Approval level assigned to each approver depending on the allocated amount. |
| 3 | `APPROVAL_LINE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 4 | `CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to class node table. |
| 5 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 6 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was was inserted. |
| 8 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 9 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 10 | `DESCRIPTION` | VARCHAR(40) |  |  | Approval description. |
| 11 | `MIN_APPROVAL_AMOUNT` | DOUBLE |  |  | Minimum approval amount. |
| 12 | `MM_APPROVAL_ID` | DOUBLE | NOT NULL |  | Group key, set of approval lines. |
| 13 | `MM_APPROVAL_IND` | DOUBLE |  |  | Set to 1 as an approval default. Set to 0 otherwise. Used to recognize a regular approval from a default one. |
| 14 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization that the approval is tied too. Foreign key to organization table. |
| 15 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key, the prsnl_id of the person from the personnel table (prsnl) |
| 16 | `SKIP_IND` | DOUBLE |  |  | Indicates the corresponding user or person as the approver. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VALIDATION_IND` | DOUBLE |  |  | Used to determine if a password validation is required for an approver. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

