# PCT_CARE_TEAM

> Stores the current and historical build for the patient care teams, which are comprised of a Medical Service, a Personnel Group, an Encounter Personnel Relation, and Personnel.

**Description:** Physician Care Team  
**Table type:** REFERENCE  
**Primary key:** `PCT_CARE_TEAM_ID`  
**Columns:** 16  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is considered valid as active current data. This may be valued with the date that the row became active. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The facility code of the care team |
| 5 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 6 | `ORIG_PCT_TEAM_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the care team information. This field will always point back to the original value created. This may be used to find the correct version when combined with the begin and end effective dates and times |
| 7 | `PCT_CARE_TEAM_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the PCT_CARE_TEAM table. |
| 8 | `PCT_MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The medical service of the care team. |
| 9 | `PCT_ROLE_CD` | DOUBLE | NOT NULL |  | The role that the provider played for this encounter. |
| 10 | `PCT_TEAM_CD` | DOUBLE | NOT NULL |  | The team that belongs to the specified medical service. |
| 11 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that is a member of the team. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORIG_PCT_TEAM_ID` | [PCT_CARE_TEAM](PCT_CARE_TEAM.md) | `PCT_CARE_TEAM_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CN_DCP_SHIFT_ASSIGNMENT_ST](CN_DCP_SHIFT_ASSIGNMENT_ST.md) | `PCT_CARE_TEAM_ID` |
| [DCP_SHIFT_ASSIGNMENT](DCP_SHIFT_ASSIGNMENT.md) | `PCT_CARE_TEAM_ID` |
| [PCT_CARE_TEAM](PCT_CARE_TEAM.md) | `ORIG_PCT_TEAM_ID` |
| [PCT_IPASS](PCT_IPASS.md) | `PCT_CARE_TEAM_ID` |

