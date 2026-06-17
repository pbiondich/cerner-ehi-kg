# HPD_MEMBERSHIP

> Stores the membership relations between a provider (HPD_PROVIDER) and an organization (HPD_ORGANIZATION)

**Description:** Healthcare Provider Directory Membership  
**Table type:** REFERENCE  
**Primary key:** `HPD_MEMBERSHIP_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `HPD_MEMBERSHIP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `HPD_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key that corresponds to a single row on the HPD_ORGANIZATION table |
| 4 | `HPD_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key that corresponds to a single row on the HPD_PROVIDER table |
| 5 | `REVISION_NBR` | DOUBLE | NOT NULL |  | Current revision of the table. This should be incremented 1 higher than the highest revision on the table. All rows in the same update should have the same revision. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HPD_ORGANIZATION_ID` | [HPD_ORGANIZATION](HPD_ORGANIZATION.md) | `HPD_ORGANIZATION_ID` |
| `HPD_PROVIDER_ID` | [HPD_PROVIDER](HPD_PROVIDER.md) | `HPD_PROVIDER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HPD_MEMBER_SERVICE_RELTN](HPD_MEMBER_SERVICE_RELTN.md) | `HPD_MEMBERSHIP_ID` |
| [HPD_MEMBER_SPECIALTY_RELTN](HPD_MEMBER_SPECIALTY_RELTN.md) | `HPD_MEMBERSHIP_ID` |

