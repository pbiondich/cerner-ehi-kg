# ENTITY_DETAIL

> Contains the primary key attributes information of all the child entities rows that were combined.

**Description:** Entity Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Contains the primary key attribute name. |
| 2 | `DATA_CHAR` | VARCHAR(100) |  |  | Contains the value of the character data type primary key attribute stored in COLUMN_NAME. |
| 3 | `DATA_DATE` | DATETIME |  |  | Contains the value of the date data type primary key attribute stored in COLUMN_NAME. |
| 4 | `DATA_NUMBER` | DOUBLE |  |  | Contains the value of the number or float data type primary key attribute stored in COLUMN_NAME. |
| 5 | `DATA_TYPE` | VARCHAR(30) | NOT NULL |  | The data type of the primary key attribute stored in COLUMN_NAME. |
| 6 | `ENTITY_ID` | DOUBLE | NOT NULL |  | This is the value of entity_id of COMBINE_DETAIL table. It is an internal system assigned number. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

