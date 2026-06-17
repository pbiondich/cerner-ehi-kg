# DM_TEXT_FIND_DETAIL

> This table will store meta-data Details about the new Text Search tool owned by DM

**Description:** DM_TEXT_FIND_DETAIL  
**Table type:** REFERENCE  
**Primary key:** `DM_TEXT_FIND_DETAIL_ID`  
**Columns:** 15  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DETAIL_DESCRIPTION` | VARCHAR(100) |  |  | Description of the Detail record |
| 3 | `DETAIL_MEANING` | VARCHAR(20) | NOT NULL |  | Contains a Meaning used to identify the row |
| 4 | `DETAIL_SCRIPT_NAME` | VARCHAR(30) |  |  | Holds a script name to retrieve data, when query can¿t be used |
| 5 | `DETAIL_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key back to LONG_TEXT_REFERENCE that contains query to search data. |
| 6 | `DETAIL_TYPE_FLAG` | DOUBLE | NOT NULL |  | A flag that indicates what type of detail row this is. |
| 7 | `DM_TEXT_FIND_DETAIL_ID` | DOUBLE | NOT NULL | PK | Primary Key for table |
| 8 | `DM_TEXT_FIND_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key back to DM_TEXT_FIND table |
| 9 | `FREQUENCY` | DOUBLE |  |  | Contains the frequency in which detail should be run in server |
| 10 | `MULTI_NODE_IND` | DOUBLE | NOT NULL |  | This column will indicate whether this report can be run on multiple nodes. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DETAIL_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `DM_TEXT_FIND_ID` | [DM_TEXT_FIND](DM_TEXT_FIND.md) | `DM_TEXT_FIND_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [DM_TEXT_FIND_DATA](DM_TEXT_FIND_DATA.md) | `DM_TEXT_FIND_DETAIL_ID` |
| [DM_TEXT_FIND_DTL_QUERY_R](DM_TEXT_FIND_DTL_QUERY_R.md) | `DM_TEXT_FIND_DETAIL_ID` |
| [DM_TEXT_FIND_LOG](DM_TEXT_FIND_LOG.md) | `DM_TEXT_FIND_DETAIL_ID` |
| [DM_TEXT_FIND_QUEUE](DM_TEXT_FIND_QUEUE.md) | `DM_TEXT_FIND_DETAIL_ID` |
| [DM_TEXT_FIND_QUEUE_HIST](DM_TEXT_FIND_QUEUE_HIST.md) | `DM_TEXT_FIND_DETAIL_ID` |
| [DM_TEXT_FIND_STRUCT](DM_TEXT_FIND_STRUCT.md) | `DM_TEXT_FIND_DETAIL_ID` |
| [DM_TEXT_FIND_SUMMARY](DM_TEXT_FIND_SUMMARY.md) | `DM_TEXT_FIND_DETAIL_ID` |

