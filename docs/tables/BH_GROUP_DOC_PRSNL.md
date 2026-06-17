# BH_GROUP_DOC_PRSNL

> The personnel that are assoicated to a Behavioral Health Group.

**Description:** Behavioral Health Group Documentation Personnel  
**Table type:** ACTIVITY  
**Primary key:** `BH_GROUP_DOC_PRSNL_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSOC_PRSNL_FULL_NAME` | VARCHAR(200) | NOT NULL |  | Name of personnel if they are not part of the organization. |
| 2 | `ASSOC_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person who is a part of the therapy session as either a facilitator or a cosigner. |
| 3 | `ASSOC_PRSNL_TYPE_FLAG` | DOUBLE | NOT NULL |  | The role that this personnel plays in the group. |
| 4 | `BH_GROUP_DOC_ID` | DOUBLE | NOT NULL | FK→ | The group that this personnel is assigned a role for. |
| 5 | `BH_GROUP_DOC_PRSNL_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BH_GROUP_DOC_PRSNL table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `VOLUNTEER_IND` | DOUBLE | NOT NULL |  | Indicates if this person is volunteering on the group. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSOC_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `BH_GROUP_DOC_ID` | [BH_GROUP_DOC](BH_GROUP_DOC.md) | `BH_GROUP_DOC_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BH_GROUP_DOC_PRSNL_ACT](BH_GROUP_DOC_PRSNL_ACT.md) | `BH_GROUP_DOC_PRSNL_ID` |

