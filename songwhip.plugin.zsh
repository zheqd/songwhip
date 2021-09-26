SONGWHIP_PLUGIN_DIR=${0:h}

function sw() {
    python3 $SONGWHIP_PLUGIN_DIR/songwhip.py $@
}
