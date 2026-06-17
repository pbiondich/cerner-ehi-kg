# SCH_ORG_SECURITY

> Sch_org_security is used to store the associations between scheduling objects such as scheduling slot type, schedule resource, scheduling default template and organizations so that we can build the organization security around these scheduling objects.

**Description:** Scheduling Organization Security  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Identifier of organization which is used to associated to the scheduling objects. |
| 2 | `PARENT1_ID` | DOUBLE | NOT NULL |  | Identifier of parent 1 table. |
| 3 | `PARENT1_TABLE` | VARCHAR(30) | NOT NULL |  | The scheduling table name which we can use to build organization security, currently we are going to support only "SCH_SLOT_TYPE", "SCH_DEF_SCHED", "SCH_RESOURCE", we will expand it to several other tables in our future iterations. |
| 4 | `SCH_ORG_SECURITY_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is internally assigned. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

