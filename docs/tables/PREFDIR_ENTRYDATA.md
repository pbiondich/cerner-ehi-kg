# PREFDIR_ENTRYDATA

> The entry data table holds information about a preference entry. This table is used to obtain the entry_id for a preference entry and to support multiple levels of search. In a hierarchical format, the search scope can be the node itself, all entries one level beneath the node or all entries below the node. The parent and the child table are included in the entry table since all the other attributes are dependent on the entry_id.

**Description:** Preference directory entry data.  
**Table type:** REFERENCE  
**Primary key:** `ENTRY_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIST_NAME` | VARCHAR(2000) | NOT NULL |  | A bottom to top hierarchical naming structure that identifies an entry uniquely from another. |
| 2 | `DIST_NAME_SHORT` | VARCHAR(255) |  |  | Short version of dist_name for building indexes on this field. |
| 3 | `ENTRY_DATA` | VARCHAR(2000) |  |  | Data associated to the dist_name. These entries are stored in a attribute:value format. |
| 4 | `ENTRY_ID` | DOUBLE | NOT NULL | PK | Unique id for each row in the table |
| 5 | `PARENT_ID` | DOUBLE | NOT NULL |  | In hierarchical structure, this id is used to identify the parent of the entry_id |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PREFDIR_ACL](PREFDIR_ACL.md) | `ENTRY_ID` |
| [PREFDIR_MULTIVALUE](PREFDIR_MULTIVALUE.md) | `ENTRY_ID` |

