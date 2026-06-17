# LIB_GRP_RELTN

> The Lib_Grp_Reltn table contains relationships between library groups. This is used within the image management area. (specifically for pull lists)

**Description:** Lirbrary Group Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LIB_GROUP_CD` | DOUBLE | NOT NULL | FK→ | The Lib_Group_Cd is a foreign key to the Library_Group table. This uniquely identifies a library group. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd is a foreign key to the Library_Group table. This uniquely identifies a library group. This allows library groups to be logically linked together for pull list purposes. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LIB_GROUP_CD` | [LIBRARY_GROUP](LIBRARY_GROUP.md) | `SERVICE_RESOURCE_CD` |
| `SERVICE_RESOURCE_CD` | [LIBRARY_GROUP](LIBRARY_GROUP.md) | `SERVICE_RESOURCE_CD` |

