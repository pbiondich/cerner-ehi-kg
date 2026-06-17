# CT_PROT_MILESTONES

> This table contains the protocol level milestones

**Description:** CT PROT MILESTONES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_CD` | DOUBLE | NOT NULL |  | The activity performed. Example: Activated By, Sent To etc. |
| 2 | `COMMITTEE_ID` | DOUBLE | NOT NULL | FK→ | The committee responsible for performing the activity |
| 3 | `CT_PROT_MILESTONES_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ct_prot_milestones table. It is an internal system assigned number. |
| 4 | `ENTITY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies whether an organization or a committee or a role is responsible for performing the action. |
| 5 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key into the Organization table. Identifies the organization responsible for the action. |
| 6 | `PERFORMED_DT_TM` | DATETIME | NOT NULL |  | The date on which the action was performed |
| 7 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | The protocol for which this belongs |
| 8 | `PROT_ROLE_CD` | DOUBLE | NOT NULL |  | The role responsoble for the action. Example: Prinicipal Investigator, Co-Investigator etc. |
| 9 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The number of the milestone |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMITTEE_ID` | [COMMITTEE](COMMITTEE.md) | `COMMITTEE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

