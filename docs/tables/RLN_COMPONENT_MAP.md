# RLN_COMPONENT_MAP

> This table will store the mapping between the client's components and the reference lab network standard components. The standard component identifier and the codeset identifier will be obtained from the cloud database

**Description:** Reference Lab Network - Component Map  
**Table type:** REFERENCE  
**Primary key:** `RLN_COMPONENT_MAP_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COMPONENT_CD` | DOUBLE | NOT NULL |  | The component (specimen type, container, collection method, unit of measure) code value. You can determine the codeset used by the codeset_flag. |
| 4 | `COMPONENT_TYPE_IDENT` | DOUBLE | NOT NULL |  | Identifies the component type. This value is from the RLN cloud database. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `ORIG_RLN_COMPONENT_MAP_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the component map information. This field will always point back to the original value created. This may be used to find the correct version when combined with the begin and end effective dates and times |
| 7 | `RLN_COMPONENT_MAP_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a mapping between the client's components and the RLN standard components. |
| 8 | `RLN_CONTRIBUTOR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related contributor source/partner lab. |
| 9 | `STANDARD_COMPONENT_IDENT` | DOUBLE | NOT NULL |  | Identifies the related standard component. The ID comes from the RLN cloud. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_RLN_COMPONENT_MAP_ID` | [RLN_COMPONENT_MAP](RLN_COMPONENT_MAP.md) | `RLN_COMPONENT_MAP_ID` |
| `RLN_CONTRIBUTOR_ID` | [RLN_CONTRIBUTOR](RLN_CONTRIBUTOR.md) | `RLN_CONTRIBUTOR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RLN_COMPONENT_MAP](RLN_COMPONENT_MAP.md) | `ORIG_RLN_COMPONENT_MAP_ID` |

