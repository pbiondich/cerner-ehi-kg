# MP_COMPONENT

> Contains the components which are associated to MPage groups. Contains all of the necessary identifying information for a component.

**Description:** MP COMPONENT  
**Table type:** REFERENCE  
**Primary key:** `MP_COMPONENT_ID`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARTIFACT_IDENT` | VARCHAR(128) | NOT NULL |  | Corresponds to the Maven identifier for a maven artifact, in this case the component |
| 2 | `FILTER_MEAN` | VARCHAR(30) |  |  | Identifies the bedrock and prefMaint settings to the page that the component is on. |
| 3 | `MP_COMPONENT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `MP_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key value from the mp_group table. |
| 5 | `TOKEN_IDENT` | VARCHAR(30) | NOT NULL |  | A small string that is used to identify this component in a URL for the static content web app. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VERSION_TXT` | VARCHAR(30) | NOT NULL |  | The maven artifact version string for this component. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MP_GROUP_ID` | [MP_GROUP](MP_GROUP.md) | `MP_GROUP_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MP_COMPONENT_COMPONENT_R](MP_COMPONENT_COMPONENT_R.md) | `CHILD_MP_COMPONENT_ID` |
| [MP_COMPONENT_COMPONENT_R](MP_COMPONENT_COMPONENT_R.md) | `MP_COMPONENT_ID` |
| [MP_COMPONENT_UTILITY_R](MP_COMPONENT_UTILITY_R.md) | `MP_COMPONENT_ID` |

