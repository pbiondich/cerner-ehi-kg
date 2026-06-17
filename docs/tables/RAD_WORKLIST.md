# RAD_WORKLIST

> Radiology reading worklist

**Description:** This table defines a description for a radiologists reading worklist.  
**Table type:** REFERENCE  
**Primary key:** `RAD_WORKLIST_ID`  
**Columns:** 9  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 2 | `RAD_WORKLIST_ID` | DOUBLE | NOT NULL | PK | The rad_config_data_id uniquely identifies a row in the Rad_config_data table. It serves no other purpose other than to uniquely identify the row. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `WORKLIST_NAME` | VARCHAR(200) |  |  | The visual display name of the worklist |
| 9 | `WORKLIST_TYPE_IND` | DOUBLE |  |  | *** OBSOLETE *** Indicate if this worklist is shared or private. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RAD_WORKLIST_FAVORITES](RAD_WORKLIST_FAVORITES.md) | `RAD_WORKLIST_ID` |
| [RAD_WORKLIST_FILTER](RAD_WORKLIST_FILTER.md) | `RAD_WORKLIST_ID` |
| [RAD_WORKLIST_SECTION_R](RAD_WORKLIST_SECTION_R.md) | `RAD_WORKLIST_ID` |

