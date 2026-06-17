# CT_MILESTONES

> This table is used to store the milestones attached to an amendment

**Description:** CT MILESTONES  
**Table type:** REFERENCE  
**Primary key:** `CT_MILESTONES_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_CD` | DOUBLE | NOT NULL |  | The activity related to the milestone. Example: Activate By, Approved By etc. |
| 2 | `COMMITTEE_ID` | DOUBLE | NOT NULL | FK→ | The committee performing the activity |
| 3 | `CT_MILESTONES_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ct_milestones table. It is an internal system assigned number. |
| 4 | `ENTITY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies whether an organization or a committee or a role is responsible for performing the action. |
| 5 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key into the Organization table. Identifies the organization responsible for the action. |
| 6 | `PERFORMED_DT_TM` | DATETIME | NOT NULL |  | The date and time on which the action was performed |
| 7 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | The amendment to which the milestone belongs |
| 8 | `PROT_ROLE_CD` | DOUBLE | NOT NULL |  | The role responsoble for the action. Example: Prinicipal Investigator, Co-Investigator etc. |
| 9 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The number of the milestone. A milestone for an amendment can have any number from 1 to the number of milestones. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMITTEE_ID` | [COMMITTEE](COMMITTEE.md) | `COMMITTEE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PROT_SUSPENSION](PROT_SUSPENSION.md) | `CT_MILESTONES_ID` |

